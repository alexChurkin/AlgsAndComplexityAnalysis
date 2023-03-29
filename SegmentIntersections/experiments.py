import time

from algorithms import intersectionNaive, intersectionEffective
from assist.advanced_drawing import drawPlot, showPlot, usePlotLegend
from assist.random_segments import generateRandomSegments, MODE_RANDOM_1, MODE_RANDOM_2


def runExperiment1():
    xValues = []
    yValuesNaive = []
    yValuesEffective = []

    print("Эксперимент 1...")
    for n in range(1, 10_002, 100):
        kSegments, _, _, otherSegments \
            = generateRandomSegments(MODE_RANDOM_1, n)
        segments = []
        segments += kSegments
        segments += otherSegments

        t1Start = time.time()
        intersectionExists1, s1, s2 = intersectionNaive(segments)
        t1Finish = time.time()

        t2Start = time.time()
        intersectionExists2, s1, s2 = intersectionEffective(segments)
        t2Finish = time.time()

        if intersectionExists1 != intersectionExists2:
            raise Exception("Something went wrong!")

        xValues.append(n)
        yValuesNaive.append(t1Finish - t1Start)
        yValuesEffective.append(t2Finish - t2Start)

    drawPlot(xValues, yValuesNaive, clr="b", label="Naive")
    drawPlot(xValues, yValuesEffective, clr="green", label="Effective")
    usePlotLegend()
    showPlot(title="Эксперимент 1: n = 1...10^4 + 1 (шаг 100)",
             xLabel="Число n (отрезков)", yLabel="Время t (с)")


def runExperiment2():
    xValues = []
    yValuesNaive = []
    yValuesEffective = []

    print("Эксперимент 2...")
    for k in range(1, 202, 50):
        kSegments, segK, segKPlus1, otherSegments \
            = generateRandomSegments(MODE_RANDOM_1, n=503, k=k)
        segments = []
        segments += kSegments
        if segK is not None and segKPlus1 is not None:
            segments.append(segK)
            segments.append(segKPlus1)
        segments += otherSegments

        t1Start = time.time()
        intersectionExists1, s1, s2 = intersectionNaive(segments)
        t1Finish = time.time()

        t2Start = time.time()
        intersectionExists2, s1, s2 = intersectionEffective(segments)
        t2Finish = time.time()

        if intersectionExists1 != intersectionExists2:
            raise Exception("Something went wrong!")

        xValues.append(k)
        yValuesNaive.append(t1Finish - t1Start)
        yValuesEffective.append(t2Finish - t2Start)

    drawPlot(xValues, yValuesNaive, clr="b", label="Naive")
    drawPlot(xValues, yValuesEffective, clr="green", label="Effective")
    usePlotLegend()
    showPlot(title="Эксперимент 2: n = 503, k = 1...201 (шаг 50)",
             xLabel="Число k (непересекающихся отрезков)", yLabel="Время t (с)")


def runExperiment3():
    xValues = []
    yValuesNaive = []
    yValuesEffective = []

    print("Эксперимент 3...")
    for n in range(1, 1002, 100):
        kSegments, _, _, otherSegments \
            = generateRandomSegments(MODE_RANDOM_2, n=n, r=0.001)
        segments = []
        segments += kSegments
        segments += otherSegments

        t1Start = time.time()
        intersectionExists1, s11, s12 = intersectionNaive(segments)
        t1Finish = time.time()

        t2Start = time.time()
        intersectionExists2, s21, s22 = intersectionEffective(segments)
        t2Finish = time.time()

        if intersectionExists1 != intersectionExists2:
            """for seg in segments:
                drawSegment(seg)

            if intersectionExists1:
                drawSegment(s11, 'r')
                drawSegment(s12, 'r')
                print(s11)
                print(s12)

            if intersectionExists2:
                drawSegment(s11, 'cyan')
                drawSegment(s12, 'cyan')
                print(s21)
                print(s22)
            showPlot()
            return"""
            raise Exception("Something went wrong!")

        xValues.append(n)
        yValuesNaive.append(t1Finish - t1Start)
        yValuesEffective.append(t2Finish - t2Start)

    drawPlot(xValues, yValuesNaive, clr="b", label="Naive")
    drawPlot(xValues, yValuesEffective, clr="green", label="Effective")
    usePlotLegend()
    showPlot(title="Эксперимент 3: n = 1...1001 (шаг 100), r = 0.001",
             xLabel="Число n (отрезков)", yLabel="Время t (с)")


def runExperiment4():
    xValues = []
    yValuesNaive = []
    yValuesEffective = []

    print("Эксперимент 4...")
    for r in [x / 1000.0 for x in range(1, 11, 1)]:
        kSegments, _, _, otherSegments \
            = generateRandomSegments(MODE_RANDOM_2, n=1000, r=r)
        segments = []
        segments += kSegments
        segments += otherSegments

        t1Start = time.time()
        intersectionExists1, s11, s12 = intersectionNaive(segments)
        t1Finish = time.time()

        t2Start = time.time()
        intersectionExists2, s21, s22 = intersectionEffective(segments)
        t2Finish = time.time()

        if intersectionExists1 != intersectionExists2:
            raise Exception("Something went wrong!")

        xValues.append(r)
        yValuesNaive.append(t1Finish - t1Start)
        yValuesEffective.append(t2Finish - t2Start)

    drawPlot(xValues, yValuesNaive, clr="b", label="Naive")
    drawPlot(xValues, yValuesEffective, clr="green", label="Effective")
    usePlotLegend()
    showPlot(title="Эксперимент 4: n = 1000, r = 0.001...0.01 (шаг 0.001)",
             xLabel="Длина отрезка r", yLabel="Время t (с)")
