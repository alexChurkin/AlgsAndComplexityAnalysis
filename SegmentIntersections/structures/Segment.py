from structures.Point import *


def epsilon_eq(x, y, epsilon):
    return abs(x - y) <= epsilon


class Segment(object):
    def __init__(self, point1, point2):
        if point1 < point2:
            self.startPoint = point1
            self.endPoint = point2
        else:
            self.startPoint = point2
            self.endPoint = point1

        if self.endPoint.x - self.startPoint.x != 0:
            self.slope = round((self.endPoint.y - self.startPoint.y) / (self.endPoint.x - self.startPoint.x), 6)
        else:
            self.slope = float("inf")

    def containsPoint(self, point):
        """
        Принимает: point
        Возвращает: True, если точка принадлежит self (отрезку)
        """
        return self.startPoint.distanceFrom(self.endPoint) == (
                self.startPoint.distanceFrom(point) + point.distanceFrom(self.endPoint))

    def intersects(self, otherSeg):
        """
        Принимает: otherSeg
        Возвращает: False, если self не пересекает otherSeg. Иначе - True.
        """
        orientation1 = Point.orientation(self.startPoint, self.endPoint, otherSeg.startPoint)
        orientation2 = Point.orientation(self.startPoint, self.endPoint, otherSeg.endPoint)
        orientation3 = Point.orientation(otherSeg.startPoint, otherSeg.endPoint, self.startPoint)
        orientation4 = Point.orientation(otherSeg.startPoint, otherSeg.endPoint, self.endPoint)

        if orientation1 != orientation2 and orientation3 != orientation4:
            return True

        if orientation1 == Orientation.ZERO and self.containsPoint(otherSeg.startPoint):
            return True

        if orientation2 == Orientation.ZERO and self.containsPoint(otherSeg.endPoint):
            return True

        if orientation3 == Orientation.ZERO and otherSeg.containsPoint(self.startPoint):
            return True

        if orientation4 == Orientation.ZERO and otherSeg.containsPoint(self.endPoint):
            return True

        return False

    def notIntersects(self, otherSeg):
        return not self.intersects(otherSeg)

    def intersectsAtLeastOne(self, segments):
        for segment in segments:
            if self.intersects(segment):
                return True
        return False

    def notIntersectsAny(self, segments):
        return not self.intersectsAtLeastOne(segments)

    def calcYValueByX(self, x):
        """
            По данному значению x вычисляет значение y соответствующей точки,
            принадлежащей собственно отрезку
            (в предположении, что x корректен)
        """
        if self.slope == 0:
            return self.startPoint.y

        st = self.startPoint
        en = self.endPoint

        if st.x - en.x != 0:
            return round((en.y * st.x - en.x * st.y - en.y * x + st.y * x) / (st.x - en.x), 7)
        else:
            return float("inf")

    def __lt__(self, other):
        """
            Оператор < для отрезков. A < B, если
            ордината A точки пересечения с заметающей прямой меньше, чем
            ордината B точки пересечения с заметающей прямой.
            Если точки пересечения с заметающей прямой накладываются, то
            A < B тогда, когда наклон (slope) A меньше.
        """
        # Считается, что из двух точек начала отрезков заметающая прямая
        # проходит по наиболее правой
        lineSweepPos = max(self.startPoint.x, other.startPoint.x)

        selfY = self.calcYValueByX(lineSweepPos)
        otherY = other.calcYValueByX(lineSweepPos)

        if epsilon_eq(selfY, otherY, 0.000001):
            return self.slope < other.slope
        else:
            return selfY < otherY

    def __str__(self):
        return f"startPoint: {self.startPoint}, endPoint: {self.endPoint}"
