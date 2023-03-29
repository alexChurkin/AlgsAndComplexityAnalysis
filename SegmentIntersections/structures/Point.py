import math
from enum import Enum


class Orientation(Enum):
    CLOCKWISE = 1
    ZERO = 0
    COUNTER_CLOCKWISE = -1


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceFrom(self, otherPoint):
        return math.hypot(otherPoint.x - self.x, otherPoint.y - self.y)

    """
    Операторы сравнения для точек (меньшей считается точка, которая
    меньше лексикографически: (x1, y1) < (x2, y2), если x1 < x2 или x1 == x2 & y1 < y2
    """

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return self > other or self == other

    @staticmethod
    def orientation(p1, p2, p3) -> Orientation:
        """
            Вычисление ориентации треугольника.
        """
        val = round((p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y), 12)

        if val < 0:
            return Orientation.COUNTER_CLOCKWISE
        elif val == 0:
            return Orientation.ZERO
        else:
            return Orientation.CLOCKWISE

    def __str__(self):
        return f"({self.x}, {self.y})"
