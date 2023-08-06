##############################################################
# Convenience functions for general spatial applications
# John Truckenbrodt, 2016-2018
##############################################################
import math
import os
from osgeo import osr, gdal, ogr

osr.UseExceptions()
ogr.UseExceptions()


def crsConvert(crsIn, crsOut):
    """
    convert between different types of spatial references

    Parameters
    ----------
    crsIn: int, str or :osgeo:class:`osr.SpatialReference`
        the input CRS
    crsOut: {'wkt', 'proj4', 'epsg', 'osr', 'opengis' or 'prettyWkt'}
        the output CRS type

    Returns
    -------
    int, str or :osgeo:class:`osr.SpatialReference`
        the output CRS

    Examples
    --------
    convert an integer EPSG code to PROJ4:

    >>> crsConvert(4326, 'proj4')
    '+proj=longlat +datum=WGS84 +no_defs '

    convert a PROJ4 string to an opengis URL:

    >>> crsConvert('+proj=longlat +datum=WGS84 +no_defs ', 'opengis')
    'http://www.opengis.net/def/crs/EPSG/0/4326'

    convert the opengis URL back to EPSG:

    >>> crsConvert('http://www.opengis.net/def/crs/EPSG/0/4326', 'epsg')
    4326

    """
    if isinstance(crsIn, osr.SpatialReference):
        srs = crsIn.Clone()
    else:
        srs = osr.SpatialReference()
        try:
            if 'opengis.net/def/crs/EPSG/0/' in str(crsIn):
                crsIn = int(os.path.basename(crsIn.strip('/')))
            srs.ImportFromEPSG(crsIn)
        except (TypeError, RuntimeError):
            try:
                srs.ImportFromWkt(crsIn)
            except (TypeError, RuntimeError):
                try:
                    srs.ImportFromProj4(crsIn)
                except (TypeError, RuntimeError):
                    raise TypeError('crsIn not recognized; must be of type WKT, PROJ4 or EPSG')
    if crsOut == 'wkt':
        return srs.ExportToWkt()
    elif crsOut == 'prettyWkt':
        return srs.ExportToPrettyWkt()
    elif crsOut == 'proj4':
        return srs.ExportToProj4()
    elif crsOut == 'epsg':
        srs.AutoIdentifyEPSG()
        return int(srs.GetAuthorityCode(None))
    elif crsOut == 'opengis':
        srs.AutoIdentifyEPSG()
        return 'http://www.opengis.net/def/crs/EPSG/0/{}'.format(srs.GetAuthorityCode(None))
    elif crsOut == 'osr':
        return srs
    else:
        raise ValueError('crsOut not recognized; must be either wkt, proj4, opengis or epsg')


def haversine(lat1, lon1, lat2, lon2):
    """
    compute the distance in meters between two points in latlon

    Parameters
    ----------
    lat1: int or float
        the latitude of point 1
    lon1: int or float
        the longitude of point 1
    lat2: int or float
        the latitude of point 2
    lon2: int or float
        the longitude of point 2

    Returns
    -------
    float
        the distance between point 1 and point 2 in meters

    """
    radius = 6371000
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    a = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return radius * c


def gdalwarp(src, dst, options):
    """
    a simple wrapper for :osgeo:func:`gdal.Warp`

    Parameters
    ----------
    src: str, :osgeo:class:`ogr.DataSource` or :osgeo:class:`gdal.Dataset`
        the input data set
    dst: str
        the output data set
    options: dict
        additional parameters passed to gdal.Warp; see :osgeo:func:`gdal.WarpOptions`

    Returns
    -------

    """
    try:
        out = gdal.Warp(dst, src, options=gdal.WarpOptions(**options))
    except RuntimeError as e:
        raise RuntimeError('{}:\n  src: {}\n  dst: {}\n  options: {}'.format(str(e), src, dst, options))
    out = None


def gdalbuildvrt(src, dst, options=None, void=True):
    """
    a simple wrapper for :osgeo:func:`gdal.BuildVRT`

    Parameters
    ----------
    src: str, list, :osgeo:class:`ogr.DataSource` or :osgeo:class:`gdal.Dataset`
        the input data set(s)
    dst: str
        the output data set
    options: dict
        additional parameters passed to gdal.BuildVRT; see :osgeo:func:`gdal.BuildVRTOptions`
    void: bool
        just write the results and don't return anything? If not, the spatial object is returned

    Returns
    -------

    """
    options = {} if options is None else options
    out = gdal.BuildVRT(dst, src, options=gdal.BuildVRTOptions(**options))
    if void:
        out = None
    else:
        return out


def gdal_translate(src, dst, options):
    """
    a simple wrapper for `gdal.Translate <https://gdal.org/python/osgeo.gdal-module.html#Translate>`_

    Parameters
    ----------
    src: str, :osgeo:class:`ogr.DataSource` or :osgeo:class:`gdal.Dataset`
        the input data set
    dst: str
        the output data set
    options: dict
        additional parameters passed to gdal.Translate;
        see `gdal.TranslateOptions <http://gdal.org/python/osgeo.gdal-module.html#TranslateOptions>`_

    Returns
    -------

    """
    out = gdal.Translate(dst, src, options=gdal.TranslateOptions(**options))
    out = None


def ogr2ogr(src, dst, options):
    """
    a simple wrapper for gdal.VectorTranslate aka `ogr2ogr <https://www.gdal.org/ogr2ogr.html>`_

    Parameters
    ----------
    src: str or :osgeo:class:`ogr.DataSource`
        the input data set
    dst: str
        the output data set
    options: dict
        additional parameters passed to gdal.VectorTranslate;
        see `gdal.VectorTranslateOptions <http://gdal.org/python/osgeo.gdal-module.html#VectorTranslateOptions>`_

    Returns
    -------

    """
    out = gdal.VectorTranslate(dst, src, options=gdal.VectorTranslateOptions(**options))
    out = None


def gdal_rasterize(src, dst, options):
    """
    a simple wrapper for gdal.Rasterize

    Parameters
    ----------
    src: str or :osgeo:class:`ogr.DataSource`
        the input data set
    dst: str
        the output data set
    options: dict
        additional parameters passed to gdal.Rasterize; see :osgeo:func:`gdal.RasterizeOptions`

    Returns
    -------

    """
    out = gdal.Rasterize(dst, src, options=gdal.RasterizeOptions(**options))
    out = None


def coordinate_reproject(x, y, s_crs, t_crs):
    """
    reproject a coordinate from one CRS to another
    
    Parameters
    ----------
    x: int or float
        the X coordinate component
    y: int or float
        the Y coordinate component
    s_crs: int, str or :osgeo:class:`osr.SpatialReference`
        the source CRS. See :func:`~spatialist.auxil.crsConvert` for options.
    t_crs: int, str or :osgeo:class:`osr.SpatialReference`
        the target CRS. See :func:`~spatialist.auxil.crsConvert` for options.

    Returns
    -------

    """
    source = crsConvert(s_crs, 'osr')
    target = crsConvert(t_crs, 'osr')
    transform = osr.CoordinateTransformation(source, target)
    point = ogr.CreateGeometryFromWkt('POINT ({0} {1})'.format(x, y))
    point.Transform(transform)
    return point.GetX(), point.GetY()
