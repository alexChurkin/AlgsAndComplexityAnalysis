import matplotlib.pyplot as plt

from structures.Segment import Segment


def drawSegment(segment: Segment, clr="b"):
    xValues = [segment.startPoint.x, segment.endPoint.x]
    yValues = [segment.startPoint.y, segment.endPoint.y]
    plt.plot(xValues, yValues, linestyle="-", markersize=0.1, color=clr)


def drawPlot(xValues: list[float], yValues: list[float], clr="b", label=""):
    plt.plot(xValues, yValues, linestyle="-", markersize=0.2, color=clr, label=label)


def usePlotLegend():
    plt.legend()


def showPlot(title: str = "График", xLabel: str = "Ось X", yLabel: str = "Ось Y"):
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid()
    plt.show()
