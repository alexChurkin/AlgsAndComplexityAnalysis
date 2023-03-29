import math

from assist.advanced_drawing import drawSegment
from assist.advanced_input import readInt, readFloat
from experiments import *
from structures.Segment import Segment, Point

MODE_MANUAL = 3
MODE_STAT = 4


# Меню
def showMenu() -> int:
    print()
    print("Меню:")
    print("-------------------------------------------------")
    print("1. Автогенерация отрезков с псевдослучайными координатами концов из единичного квадрата")
    print("2. Автогенерация отрезков с псевдослучайными координатами центров из единичного квадрата\n   и "
          "псевдослучайными углами между собой и осью абсцисс")
    print("3. Ручной ввод отрезков в формате x1 y1 x2 y2 ...")
    print("-------------------------------------------------")
    print("4. Построить графики")
    print("-------------------------------------------------")
    print()
    mode: int = readInt("Ваш выбор: ",
                        minimum=1, maximum=4)
    return mode


# Запуск одиночного эксперимента
def runSingleExperiment(mode: int):
    segments = []

    n: int = readInt("Введите число [2, inf) отрезков: n = ",
                     minimum=2, maximum=math.inf, includeR=False)

    # >>> Выбран автоматический способ задания отрезков
    if mode == MODE_RANDOM_1 or mode == MODE_RANDOM_2:
        r: float = -1
        if mode == MODE_RANDOM_2:
            r = readFloat("Длина (0, inf) отрезков: r = ",
                          minimum=0, maximum=math.inf, includeL=False, includeR=False)

        k = readInt(f"Введите число [0, {n - 2}] отрезков, не пересекающихся ни с какими: k = ",
                    minimum=0, maximum=n - 2)

        kSegments, segK, segKPlus1, otherSegments = generateRandomSegments(mode, n, k, r)

        # Добавление всех отрезков в общий список
        segments += kSegments
        if segK is not None and segKPlus1 is not None:
            segments.append(segK)
            segments.append(segKPlus1)
        segments += otherSegments

        print()
        print("Сгенерирован набор отрезков:")
        for s in segments:
            print(f"{s.startPoint.x} {s.startPoint.y} {s.endPoint.x} {s.endPoint.y}")
        print()

        # Отрисовка всех отрезков
        # > Синие не пересекаются ни с какими,
        # > красные обязательно пересекаются как минимум между собой,
        # > зелёные могут пересекаться между собой и с красными
        for seg in kSegments:
            drawSegment(seg)
        for seg in otherSegments:
            drawSegment(seg, "green")
        if segK is not None and segKPlus1 is not None:
            drawSegment(segK, "red")
            drawSegment(segKPlus1, "red")

    # >>> Выбран ручной способ задания отрезков
    else:
        for i in range(0, n):
            line = input().split(sep=' ')
            newSegment = Segment(Point(float(line[0]), float(line[1])),
                                 Point(float(line[2]), float(line[3])))
            segments.append(newSegment)
            drawSegment(newSegment)

    t1Start = time.time()
    intersectionExists, s1, s2 = intersectionNaive(segments)
    t1Finish = time.time()

    print()
    print(f"intersectionNaive: t = {t1Finish - t1Start}")

    if intersectionExists:
        print("Найдены пересекающиеся отрезки:")
        print(s1)
        print(s2)
    else:
        print("Пересекающихся отрезков не найдено.")

    t2Start = time.time()
    intersectionExists, s1, s2 = intersectionEffective(segments)
    t2Finish = time.time()

    print()
    print(f"intersectionEffective: t = {t2Finish - t2Start}")

    if intersectionExists:
        print("Найдены пересекающиеся отрезки:")
        print(s1)
        print(s2)
        drawSegment(s1, "cyan")
        drawSegment(s2, "cyan")
    else:
        print("Пересекающихся отрезков не найдено.")

    showPlot(title="Отрезки")


# Массовый запуск экспериментов и построение сравнительных графиков скорости работы
def runStatExperiments():
    runExperiment1()
    runExperiment2()
    runExperiment3()
    runExperiment4()


def main():
    menuResult = showMenu()

    if menuResult != MODE_STAT:
        runSingleExperiment(menuResult)
    else:
        runStatExperiments()


main()
