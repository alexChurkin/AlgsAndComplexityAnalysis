# Выполняет наивный поиск двух пересекающихся отрезков.
# Если такие найдутся, возвращает True и эти отрезки.
# Если нет - возвращает False и 2 None.
from enum import Enum

from structures.LineStatus import LineStatus
from structures.Segment import Segment


class PointType(Enum):
    START_POINT = 0
    END_POINT = 1


def intersectionNaive(segments: list[Segment]):
    for i in range(0, len(segments)):
        for j in range(i + 1, len(segments)):
            if segments[i].intersects(segments[j]):
                return True, segments[i], segments[j]
    return False, None, None


# Выполняет эффективный поиск двух пересекающихся отрезков
# Методом сканирующей прямой.
def intersectionEffective(segmentsList: list[Segment]):
    # Лексикографическая сортировка точек за O(N * logN)
    elements = [(seg.startPoint, PointType.START_POINT, seg) for seg in segmentsList] + \
               [(seg.endPoint, PointType.END_POINT, seg) for seg in segmentsList]

    elements.sort(key=lambda el: (el[0].x, el[0].y))

    lineStatus = LineStatus()

    for point, eventType, seg in elements:
        if eventType == PointType.START_POINT:
            lineStatus.insert(seg)
            """
                Дан отрезок, пересекающийся началом с заметающей прямой. Проверяем его на пересечения
                с его верхним и нижним отрезками (если они существуют).
            """
            ((intersectionPrev, prevSeg), (intersectionNext, nextSeg)) = lineStatus.adjIntersections(seg)
            if intersectionPrev:
                return True, prevSeg, seg

            if intersectionNext:
                return True, seg, nextSeg

        elif eventType == PointType.END_POINT:
            """
                Дан отрезок, пересекающийся концом с заметающей прямой. Проверяем на пересечения
                его верхние и нижние отрезки (если они существуют).
            """
            nextSeg, prevSeg = lineStatus.adjSeg(seg)
            lineStatus.remove(seg)
            if nextSeg is not None and prevSeg is not None:
                intersection = nextSeg.intersects(prevSeg)
                if intersection:
                    return True, nextSeg, prevSeg
    return False, None, None
