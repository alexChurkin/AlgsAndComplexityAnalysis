from time import time

import algorithms
from assist.advanced_drawing import drawPlot, usePlotLegend, showPlot
from assist.randint_lists import generateRandomList, generateRandomListAsc, generateRandomListDesc

RANDOM = 1
RANDOM_ASC = 2
RANDOM_DESC = 3


def runExperiment1(mode: int):
    xValues = []
    yValuesAVL = []
    yValuesRedBlack = []
    yValuesSplay = []

    q = 1
    w = 10 ** 9

    print(f"Эксперимент 1.{mode}...")
    for n in range(1, 5 * (10 ** 4) + 2, 10 ** 4):
        if mode == RANDOM:
            inputList = generateRandomList(size=n, minimum=q, maximum=w)
        elif mode == RANDOM_ASC:
            inputList = generateRandomListAsc(size=n, minimum=q, maximum=w)
        else:
            inputList = generateRandomListDesc(size=n, minimum=q, maximum=w)

        t1Start = time()
        avlSortedList = algorithms.avlSort(inputList)
        t1Finish = time()

        t2Start = time()
        redBlackSortedList = algorithms.redBlackSort(inputList)
        t2Finish = time()

        t3Start = time()
        splaySortedList = algorithms.splaySort(inputList)
        t3Finish = time()

        # Проверка, что результаты всех трёх сортировок идентичны
        # for i in range(1, len(avlSortedList)):
        #    if avlSortedList[i] != redBlackSortedList[i]:
        #        raise "Сортировка некорректна"
        #    elif avlSortedList[i] != splaySortedList[i]:
        #        raise "Сортировка некорректна (2)"

        xValues.append(n)
        yValuesAVL.append(t1Finish - t1Start)
        yValuesRedBlack.append(t2Finish - t2Start)
        yValuesSplay.append(t3Finish - t3Start)

    drawPlot(xValues, yValuesAVL, clr="r", label="АВЛ-дерево")
    drawPlot(xValues, yValuesRedBlack, clr="g", label="Красно-чёрное дерево")
    drawPlot(xValues, yValuesSplay, clr="b", label="Splay-дерево")
    usePlotLegend()
    showPlot(title=f"Эксперимент 1.{mode}: n = 1...5*10^4 + 1 (шаг 10^4)",
             xLabel="Число n (элементов)", yLabel="Время t (с)")


def runExperiment2(mode: int):
    xValues = []
    yValuesAVL = []
    yValuesRedBlack = []
    yValuesSplay = []

    n = 5 * (10 ** 3)
    q = 1

    print(f"Эксперимент 2.{mode}...")
    for w in range(q, 71, 1):
        if mode == RANDOM:
            inputList = generateRandomList(size=n, minimum=q, maximum=w)
        elif mode == RANDOM_ASC:
            inputList = generateRandomListAsc(size=n, minimum=q, maximum=w)
        else:
            inputList = generateRandomListDesc(size=n, minimum=q, maximum=w)

        t1Start = time()
        avlSortedList = algorithms.avlSort(inputList)
        t1Finish = time()

        t2Start = time()
        redBlackSortedList = algorithms.redBlackSort(inputList)
        t2Finish = time()

        t3Start = time()
        splaySortedList = algorithms.splaySort(inputList)
        t3Finish = time()

        # Проверка, что результаты всех трёх сортировок идентичны
        # for i in range(1, len(avlSortedList)):
        #    if avlSortedList[i] != redBlackSortedList[i]:
        #        raise "Сортировка некорректна"
        #    elif avlSortedList[i] != splaySortedList[i]:
        #        raise "Сортировка некорректна (2)"

        xValues.append(w)
        yValuesAVL.append(t1Finish - t1Start)
        yValuesRedBlack.append(t2Finish - t2Start)
        yValuesSplay.append(t3Finish - t3Start)

    drawPlot(xValues, yValuesAVL, clr="r", label="АВЛ-дерево")
    drawPlot(xValues, yValuesRedBlack, clr="g", label="Красно-чёрное дерево")
    drawPlot(xValues, yValuesSplay, clr="b", label="Splay-дерево")
    usePlotLegend()
    showPlot(title=f"Эксперимент 2.{mode}: q = 1...70 (шаг 1)",
             xLabel="Число w (макс. возможный элемент массива)", yLabel="Время t (с)")
