from shapely.geometry import LineString, Point


class PointHash(Point):
    """Hashable Point"""

    def __hash__(self):
        return hash(self.coords[0])


class LineStringHash(LineString):
    """Hashable Linestring"""

    def __hash__(self):
        return hash(tuple(self.coords))
