from functools import reduce, partial
from itertools import combinations
from operator import add
from typing import Iterable

from shapely import wkt
from shapely.geometry.base import BaseGeometry


def find_all_intersection_points(geoms: Iterable) -> list:
    """Find all intersections of given geoms.

    Parameters
    ----------
    geoms: Iterable
        Iterable of geometries.

    Returns
    -------
    list
        List of intersection Points.
    """
    # find all pairwise intersections
    pairs = combinations(geoms, 2)
    pairwise_intersections = list(p[0].intersection(p[1]) for p in pairs)

    # split into simple and multi geometries
    multi_geoms = reduce(
        add, (list(pi.geoms) for pi in pairwise_intersections if hasattr(pi, "geoms"))
    )
    simple_geoms = list(pi for pi in pairwise_intersections if not hasattr(pi, "geoms"))

    # merge again
    intersection_points = multi_geoms + simple_geoms

    return intersection_points


def round_precision(geom: BaseGeometry, ndigits: int = 5):
    """Round a geometry to a given precision.

    See <https://gis.stackexchange.com/a/276512> for the wkt roundtrip idea.

    Parameters
    ----------
    geom: BaseGemetry
        A shapely geometry object.
    ndigits: int
        Defaults to 5 digits.

    Returns
    -------
    BaseGeometry
        Geometry object with precision reduced to the requested level.

    """
    return wkt.loads(wkt.dumps(geom, rounding_precision=ndigits))
