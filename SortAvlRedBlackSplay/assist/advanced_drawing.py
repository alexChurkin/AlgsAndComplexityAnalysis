import matplotlib.pyplot as plt


def drawPlot(xValues: list, yValues: list, clr="b", label=""):
    plt.plot(xValues, yValues, linestyle="-", markersize=0.2, color=clr, label=label)


def usePlotLegend():
    plt.legend()


def showPlot(title: str = "График", xLabel: str = "Ось X", yLabel: str = "Ось Y"):
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid()
    plt.show()
