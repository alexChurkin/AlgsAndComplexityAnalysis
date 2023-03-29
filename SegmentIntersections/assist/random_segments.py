import math
import random

from structures.Segment import Point, Segment

MODE_RANDOM_1 = 1
MODE_RANDOM_2 = 2


# Создаёт случайные отрезки по заданным параметрам
def generateRandomSegments(mode: int, n: int, k: int = 0, r: float = -1):
    kSegments: list[Segment] = []
    segK = None
    segKPlus1 = None
    otherSegments: list[Segment] = []

    def randomSegFunc():
        if mode == MODE_RANDOM_1:
            return randomUnitSquareSegment1()
        else:
            return randomUnitSquareSegment2(r)

    # Генерация отрезков от 0 до k - 1 (не пересекаются ни с какими)
    i = 0
    while i < k:
        newSeg = randomSegFunc()
        if newSeg.notIntersectsAny(kSegments):
            i += 1
            kSegments.append(newSeg)
            # print(f"Создан непересекающийся отрезок {i}")

    # Генерация отрезков k и k + 1 (пересекаются между собой + возможно, с последующими)
    if k > 0:
        while True:
            segK = randomSegFunc()
            if segK.notIntersectsAny(kSegments):
                # print(f"Создан отрезок k + 1 = {k + 1}")
                break

        while True:
            segKPlus1 = randomSegFunc()
            if segKPlus1.notIntersectsAny(kSegments) and segKPlus1.intersects(segK):
                # print(f"Создан отрезок k + 2 = {k + 2}")
                break

    # Генерация оставшихся отрезков от k + 2 до n - 1
    i = k + 2 if k > 0 else k
    while i < n:
        newSeg = randomSegFunc()
        if newSeg.notIntersectsAny(kSegments):
            i += 1
            otherSegments.append(newSeg)
            # print(f"Создан обычный отрезок {i}")

    return kSegments, segK, segKPlus1, otherSegments


# Возвращает отрезок с псевдослучайными координатами КОНЦОВ из единичного квадрата
def randomUnitSquareSegment1() -> Segment:
    return Segment(_randomUnitSquarePoint(), _randomUnitSquarePoint())


# Принимает длину r отрезка.
# Возвращает отрезок, имеющий псевдослучайные координаты ЦЕНТРА из единичного квадрата
# И псевдослучайный угол между собой и осью абсцисс
def randomUnitSquareSegment2(r: float) -> Segment:
    center = _randomUnitSquarePoint()
    alphaDeg = random.randint(0, 180)

    pointA = None
    pointB = None

    if alphaDeg == 0:
        pointA = Point(center.x - 0.5 * r, center.y)
        pointB = Point(center.x + 0.5 * r, center.y)
    elif alphaDeg == 90:
        pointA = Point(center.x, center.y + 0.5 * r)
        pointB = Point(center.x, center.y - 0.5 * r)
    elif alphaDeg == 180:
        pointA = Point(center.x + 0.5 * r, center.y)
        pointB = Point(center.x - 0.5 * r, center.y)
    elif 0 < alphaDeg < 90:
        pointA = Point(center.x + 0.5 * r * math.cos(math.radians(alphaDeg)),
                       center.y + 0.5 * r * math.sin(math.radians(alphaDeg)))
        pointB = Point(center.x - 0.5 * r * math.cos(math.radians(alphaDeg)),
                       center.y - 0.5 * r * math.sin(math.radians(alphaDeg)))
    elif 90 < alphaDeg < 180:
        betaDeg = 180 - alphaDeg
        pointA = Point(center.x - 0.5 * r * math.cos(math.radians(betaDeg)),
                       center.y + 0.5 * r * math.sin(math.radians(betaDeg)))
        pointB = Point(center.x + 0.5 * r * math.cos(math.radians(betaDeg)),
                       center.y - 0.5 * r * math.sin(math.radians(betaDeg)))

    reverse = random.choice([True, False])

    if reverse:
        return Segment(pointB, pointA)
    else:
        return Segment(pointA, pointB)


# Возвращает псевдослучайную точку из единичного квадрата
def _randomUnitSquarePoint() -> Point:
    return Point(random.random(), random.random())
