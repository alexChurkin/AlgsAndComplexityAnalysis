from time import time

from DrawingHelper import drawPlot, usePlotLegend, showPlot
from Graph import Graph


def measureDijkstra3HeapTime(graph, src):
    start = time()
    graph.dijkstra3Heap(src)
    end = time()
    return end - start


def measureDijkstraMarksTime(graph, src):
    start = time()
    graph.dijkstraMark(src)
    end = time()
    return end - start


def generatePlot(x_values, y_values_3, y_values_marks):
    drawPlot(x_values, y_values_3, clr='b', label='На 3-куче')
    drawPlot(x_values, y_values_marks, clr='r', label='На метках')
    usePlotLegend()


# Эксперимент типа 1.
# Вершин n = 101...2001 (шаг 100),
# Рёбер  m = mFunc(n)
# Веса рёбер в диапазоне от [q, r] (q = 1, r = 10^6)
def experiment1(title, mFunc):
    x_values = []
    y_values_3 = []
    y_values_marks = []

    q = 1
    r = 10 ** 6

    for n in range(101, 2101, 100):
        graph = Graph(n)
        m = mFunc(n)
        if m >= n * (n - 1):
            graph.makeComplete(q, r)
        else:
            graph.makeRandom(m // 2, q, r)

        x_values.append(n)
        y_values_3.append(measureDijkstra3HeapTime(graph, 0))
        distances1 = graph.dist.copy()
        y_values_marks.append(measureDijkstraMarksTime(graph, 0))
        distances2 = graph.dist

        if distances1 != distances2:
            raise "Ошибка: Результаты алгоритмов различны!"

        print(f"n = {n}")

    generatePlot(x_values, y_values_3, y_values_marks)
    showPlot(title=title,
             x_label='Число n (вершин)', y_label='Время t (с)')


# Эксперимент типа 2.
# Вершин n = 2001,
# Рёбер  m = 1...10^6+1 с шагом 10^5
# Веса рёбер в диапазоне от [q, r] (q = 1, r = 10^6)
def experiment2(title):
    x_values = []
    y_values_3 = []
    y_values_marks = []

    n = 2001
    q = 1
    r = 10 ** 6

    for m in range((10 ** 5) + 1, (10 ** 6) + (10 ** 5) + 1, 10 ** 5):
        graph = Graph(n)

        if m >= n * (n - 1):
            graph.makeComplete(q, r)
        else:
            graph.makeRandom(m // 2, q, r)

        x_values.append(m)
        y_values_3.append(measureDijkstra3HeapTime(graph, 0))
        distances1 = graph.dist.copy()
        y_values_marks.append(measureDijkstraMarksTime(graph, 0))
        distances2 = graph.dist

        if distances1 != distances2:
            raise "Ошибка: Результаты алгоритмов различны!"

        print(f"m = {m}")

    generatePlot(x_values, y_values_3, y_values_marks)
    showPlot(title=title,
             x_label='Число m (рёбер)', y_label='Время t (с)')


# Эксперимент типа 3.
# Вершин n = 2001,
# Рёбер  m = mFunc(n)
# Веса рёбер в диапазоне от [q, r] (q = 1, r = 1...201 с шагом 25)
def experiment3(title, mFunc):
    x_values = []
    y_values_3 = []
    y_values_marks = []

    n = 2001
    m = mFunc(n)

    q = 1

    for r in range(1, 226, 25):
        graph = Graph(n)

        if m >= n * (n - 1):
            graph.makeComplete(q, r)
        else:
            graph.makeRandom(m // 2, q, r)

        x_values.append(r)
        y_values_3.append(measureDijkstra3HeapTime(graph, 0))
        distances1 = graph.dist.copy()
        y_values_marks.append(measureDijkstraMarksTime(graph, 0))
        distances2 = graph.dist

        if distances1 != distances2:
            raise "Ошибка: Результаты алгоритмов различны!"

        print(f"r = {r}")

    generatePlot(x_values, y_values_3, y_values_marks)
    showPlot(title=title,
             x_label='Число r (макс. вес ребра)', y_label='Время t (с)')


def main():
    # 1 и 2 - эксперименты с увеличением числа вершин

    # 1
    print("Эксперимент 1.1:")
    print("................")
    experiment1('Эксперимент 1.1:\nn = 101...2001 (шаг 100), m = n^2 / 10, q = 1, r=10^6',
                lambda n: n ** 2 // 10)
    print("................")

    print("Эксперимент 1.2:")
    print("................")
    experiment1('Эксперимент 1.2:\nn = 101...2001 (шаг 100), m = n^2, q = 1, r=10^6',
                lambda n: n ** 2)
    print("................")

    # 2
    print("Эксперимент 2.1:")
    print("................")
    experiment1('Эксперимент 2.1:\nn = 101...2001 (шаг 100), m = 100 * n, q = 1, r=10^6',
                lambda n: 100 * n)
    print("................")

    print("Эксперимент 2.2:")
    print("................")
    experiment1('Эксперимент 2.2:\nn = 101...2001 (шаг 100), m = 1000 * n, q = 1, r=10^6',
                lambda n: 1000 * n)
    print("................")

    # 3 - эксперимент с увеличением числа рёбер при одинаковом числе вершин
    print("Эксперимент 3:")
    print("................")
    experiment2('Эксперимент 3:\nn = 2001, m = 10^5 + 1...10^6+1 (шаг 10^5), q = 1, r=10^6')
    print("................")

    # 4 - эксперименты с увеличением возможного разброса в значениях весов путей
    print("Эксперимент 4.1:")
    print("................")
    experiment3('Эксперимент 4.1:\nn = 2001, m = n^2, q = 1, r = 1...201 (шаг 25)',
                lambda n: n ** 2)
    print("................")

    print("Эксперимент 4.2:")
    print("................")
    experiment3('Эксперимент 4.2:\nn = 2001, m = 1000 * n, q = 1, r = 1...201 (шаг 25)',
                lambda n: 1000 * n)
    print("................")


if __name__ == '__main__':
    main()
