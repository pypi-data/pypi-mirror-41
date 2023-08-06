"""
Module for working with Geopedia OGC services
"""

import logging
import datetime

from shapely.geometry import shape as geo_shape

from .ogc import OgcImageService, MimeType
from .config import SHConfig
from .download import DownloadRequest, get_json
from .constants import CRS

LOGGER = logging.getLogger(__name__)


class GeopediaService:
    """ The class for Geopedia OGC services

    :param base_url: Base url of Geopedia REST services. If ``None``, the url specified in the configuration
                    file is taken.
    :type base_url: str or None
    """
    def __init__(self, base_url=None):
        self.base_url = SHConfig().geopedia_rest_url if base_url is None else base_url

    @staticmethod
    def _parse_layer(layer, return_wms_name=False):
        """ Helper function for parsing Geopedia layer name. If WMS name is required and wrong form is given it will
        return a string with 'ttl' at the beginning. (WMS name can also start with something else, e.g. only 't'
        instead 'ttl', therefore anything else is also allowed.) Otherwise it will parse it into a number.
        """
        if not isinstance(layer, (int, str)):
            raise ValueError("Parameter 'layer' should be an integer or a string, but {} found".format(type(layer)))

        if return_wms_name:
            if isinstance(layer, int) or layer.isdigit():
                return 'ttl{}'.format(layer)
            return layer

        if isinstance(layer, str):
            stripped_layer = layer.lstrip('tl')
            if not stripped_layer.isdigit():
                raise ValueError("Parameter 'layer' has unsupported value {}, expected an integer".format(layer))
            layer = stripped_layer

        return int(layer)


class GeopediaSession(GeopediaService):
    """ For retrieving data from Geopedia vector and raster layers it is required to make a session. This class handles
    starting and renewing of session. It provides session headers required by Geopedia REST requests.

    The session is created globally for all instances of this class. At the moment session duration is hardcoded to 1
    hour. After that this class will renew the session.
    """
    SESSION_DURATION = datetime.timedelta(hours=1)

    _session_id = None
    _session_end_timestamp = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.session_url = '{}data/v1/session/create?locale=en'.format(self.base_url)

    def get_session_headers(self, force_new_session=False):
        """ Returns session headers

        :param force_new_session: If ``True`` it will always create a new session. Otherwise it will create a new
            session only if no session exists or the previous session timed out.
        :type force_new_session: bool
        :return: A dictionary containing session headers
        :rtype: dict
        """
        return {
            'X-GPD-Session': self.get_session_id(force_new_session=force_new_session)
        }

    def get_session_id(self, force_new_session=False):
        """ Returns a session ID

        :param force_new_session: If ``True`` it will always create a new session. Otherwise it will create a new
            session only if no session exists or the previous session timed out.
        :type force_new_session: bool
        :return: A session ID string
        :rtype: str
        """
        if self._session_id is None or force_new_session or datetime.datetime.now() > self._session_end_timestamp:
            self._start_new_session()

        return self._session_id

    def _start_new_session(self):
        """ Updates the session id and calculates when the new session will end.
        """
        self._session_end_timestamp = datetime.datetime.now() + self.SESSION_DURATION
        self._session_id = get_json(self.session_url)['sessionId']


class GeopediaWmsService(GeopediaService, OgcImageService):
    """Geopedia OGC services class for providing image data. Most of the methods are inherited from
    `sentinelhub.ogc.OgcImageService` class.

    :param base_url: Base url of Geopedia WMS services. If ``None``, the url specified in the configuration
                    file is taken.
    :type base_url: str or None
    """
    def __init__(self, base_url=None):
        super().__init__(base_url=SHConfig().geopedia_wms_url if base_url is None else base_url)

    def get_request(self, request):
        """Get a list of DownloadRequests for all data that are under the given field in the table of a Geopedia layer.

        :return: list of items which have to be downloaded
        :rtype: list(DownloadRequest)
        """
        request.layer = self._parse_layer(request.layer, return_wms_name=True)

        return super().get_request(request)

    def get_dates(self, request):
        """ Geopedia does not support date queries

        :param request: OGC-type request
        :type request: WmsRequest or WcsRequest
        :return: Undefined date
        :rtype: [None]
        """
        return [None]

    def get_wfs_iterator(self):
        """ This method is inherited from OgcImageService but is not implemented.
        """
        raise NotImplementedError


class GeopediaImageService(GeopediaService):
    """Service class that provides images from a Geopedia vector layer.

    :param base_url: Base url of Geopedia REST services. If ``None``, the url
                     specified in the configuration file is taken.
    :type base_url: str or None
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.gpd_iterator = None

    def get_request(self, request):
        """Get a list of DownloadRequests for all data that are under the given field in the table of a Geopedia layer.

        :return: list of items which have to be downloaded
        :rtype: list(DownloadRequest)
        """
        return [DownloadRequest(url=self._get_url(item),
                                filename=self._get_filename(request, item),
                                data_type=request.image_format)
                for item in self._get_items(request)]

    def _get_items(self, request):
        """ Collects data from Geopedia layer and returns list of features
        """
        if request.gpd_iterator is None:
            self.gpd_iterator = GeopediaFeatureIterator(request.layer, bbox=request.bbox, base_url=self.base_url)
        else:
            self.gpd_iterator = request.gpd_iterator

        field_iter = self.gpd_iterator.get_field_iterator(request.image_field_name)
        items = []

        for field_items in field_iter:  # an image field can have multiple images

            for item in field_items:
                if not item['mimeType'].startswith('image/'):
                    continue

                mime_type = MimeType.from_string(item['mimeType'][6:])

                if mime_type is request.image_format:
                    items.append(item)

        return items

    @staticmethod
    def _get_url(item):
        return item.get('objectPath')

    @staticmethod
    def _get_filename(request, item):
        """ Creates a filename
        """
        if request.keep_image_names:
            filename = OgcImageService.finalize_filename(item['niceName'].replace(' ', '_'))
        else:
            filename = OgcImageService.finalize_filename(
                '_'.join([str(GeopediaService._parse_layer(request.layer)), item['objectPath'].rsplit('/', 1)[-1]]),
                request.image_format
            )

        LOGGER.debug("filename=%s", filename)
        return filename

    def get_gpd_iterator(self):
        """Returns iterator over info about data used for the
        GeopediaVectorRequest

        :return: Iterator of dictionaries containing info about data used in the request.
        :rtype: Iterator[dict] or None
        """
        return self.gpd_iterator


class GeopediaFeatureIterator(GeopediaService):
    """Iterator for Geopedia Vector Service

    :param layer: Geopedia layer which contains requested data
    :type layer: str
    :param bbox: Bounding box of the requested image. Its coordinates must be
                 in the CRS.POP_WEB (EPSG:3857) coordinate system.
    :type bbox: BBox
    :param query_filter: Query string used for filtering returned features.
    :type query_filter: str
    :param base_url: Base url of Geopedia REST services. If ``None``, the url specified in the configuration
        file is taken.
    :type base_url: str or None
    """
    FILTER_EXPRESSION = 'filterExpression'

    def __init__(self, layer, bbox=None, query_filter=None, **kwargs):
        super().__init__(**kwargs)

        self.layer = self._parse_layer(layer)

        self.query = {}
        if bbox is not None:
            if bbox.crs is not CRS.POP_WEB:
                bbox = bbox.transform(CRS.POP_WEB)

            self.query[self.FILTER_EXPRESSION] = 'bbox({},"EPSG:3857")'.format(bbox)
        if query_filter is not None:
            if self.FILTER_EXPRESSION in self.query:
                self.query[self.FILTER_EXPRESSION] = '{} && ({})'.format(self.query[self.FILTER_EXPRESSION],
                                                                         query_filter)
            else:
                self.query[self.FILTER_EXPRESSION] = query_filter

        self.gpd_session = GeopediaSession()
        self.features = []
        self.layer_size = None
        self.index = 0

        self.next_page_url = '{}data/v2/search/tables/{}/features'.format(self.base_url, self.layer)

    def __iter__(self):
        self.index = 0

        return self

    def __next__(self):
        if self.index == len(self.features):
            self._fetch_features()

        if self.index < len(self.features):
            self.index += 1
            return self.features[self.index - 1]

        raise StopIteration

    def __len__(self):
        """ Length of iterator is number of features which can be obtained from Geopedia with applied filters
        """
        return self.get_size()

    def _fetch_features(self):
        """ Retrieves a new page of features from Geopedia
        """
        if self.next_page_url is None:
            return

        response = get_json(self.next_page_url, post_values=self.query, headers=self.gpd_session.get_session_headers())

        self.features.extend(response['features'])
        self.next_page_url = response['pagination']['next']
        self.layer_size = response['pagination']['total']

    def get_geometry_iterator(self):
        """ Iterator over Geopedia feature geometries
        """
        for feature in self:
            yield geo_shape(feature['geometry'])

    def get_field_iterator(self, field):
        """ Iterator over the specified field of Geopedia features
        """
        for feature in self:
            yield feature['properties'].get(field, [])

    def get_size(self):
        """ Provides number of features which can be obtained. It has to fetch at least one feature from
        Geopedia services to get this information.

        :return: Size of Geopedia layer with applied filters
        :rtype: int
        """
        if self.layer_size is None:
            self._fetch_features()
        return self.layer_size
