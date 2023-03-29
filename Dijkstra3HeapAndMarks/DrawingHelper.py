import matplotlib.pyplot as plt


def drawPlot(x_values, y_values, clr='b', label=''):
    plt.plot(x_values, y_values, linestyle='-', markersize=0.2, color=clr, label=label)


def usePlotLegend():
    plt.legend()


def showPlot(title, x_label, y_label):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.show()
