from shapely.geometry import Point, LineString

from lmroute.hashable import PointHash, LineStringHash


def test_hashable_point_is_hashable():
    p = Point(1, 2)
    hp = PointHash(p)
    h = hash(hp)  # would raise error for regular Point


def test_hashable_linestring_is_hashable():
    l = LineString([(0, 1), (1, 2)])
    hl = LineStringHash(l)
    h = hash(hl)  # would raise error for regular LineString


def test_hashable_point_hashes_differ():
    p0 = PointHash(1, 2)
    p1 = PointHash(1, 3)
    p2 = PointHash(1, 2)  # same as p0
    assert hash(p0) != hash(p1)
    assert hash(p0) == hash(p2)


def test_hashable_linestrings_hashes_differ():
    l0 = LineStringHash([(1, 2), (2, 3)])
    l1 = LineStringHash([(1, 3), (2, 3)])
    l2 = LineStringHash([(1, 2), (2, 3)])  # same as l0
    assert hash(l0) != hash(l1)
    assert hash(l0) == hash(l2)


def test_set_works():
    geoms = [
        PointHash(1, 2),
        PointHash(2, 3),
        PointHash(1, 2),  # duplicate
        LineStringHash([(1, 2), (2, 3)]),
        LineStringHash([(4, 5), (2, 3)]),
        LineStringHash([(1, 2), (2, 3)]),  # duplicate
    ]
    assert len(set(geoms)) == (len(geoms) - 2)  # there's two duplicates
