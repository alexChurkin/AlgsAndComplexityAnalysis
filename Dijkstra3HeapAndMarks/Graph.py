from random import randint
from sys import maxsize

from DHeap import DHeap


# Класс графа
class Graph:
    # Инициализация графа с n вершинами
    def __init__(self, n):
        # adjList - список смежности. Хранит: u -> [(v1,w1), (v2,w2), ...,  (vn,wn)]
        self.adjList = {}
        # Число вершин графа
        self.num_nodes = n
        # Хранит расстояния до конкретной вершины от исходной
        self.dist = [0] * self.num_nodes

    # Добавление в граф ребра u -> v и u <- v
    def addEdge(self, u, v, w):
        #  Добавления ребра, идущего от звена u к v (с весом w)
        if u in self.adjList:
            self.adjList[u].append((v, w))
        else:
            self.adjList[u] = [(v, w)]

        #  Добавления ребра, идущего от звена v к u (с весом w)
        if v in self.adjList:
            self.adjList[v].append((u, w))
        else:
            self.adjList[v] = [(u, w)]

    # Делает граф полным (со случайными весами от q до r)
    def makeComplete(self, q, r):
        for u in range(self.num_nodes):
            for v in range(u + 1, self.num_nodes):
                self.addEdge(u, v, randint(q, r))

    # Заполняет граф m случайными рёбрами (со случайными весами от q до r)
    def makeRandom(self, m, q, r):
        edges = set()
        for u in range(self.num_nodes):
            for _ in range(m // self.num_nodes):
                v = randint(0, self.num_nodes - 1)
                pair = (u, v) if u < v else (v, u)

                if pair not in edges and u != v:
                    self.addEdge(u, v, randint(q, r))
                    edges.add(pair)

    # Вывод списка смежности графа на экран
    def showGraph(self):
        for u in self.adjList:
            print(u, "->", " -> ".join(
                str(f"{v}({w})") for v, w in self.adjList[u]))

    # Запуск алгоритма Дейкстры на 3-куче (из вершины src)
    def dijkstra3Heap(self, src):
        # До всех вершин назначаются расстояния от исходной как +бесконечность
        for u in self.adjList.keys():
            self.dist[u] = maxsize

        # Инициализируется троичная куча нужного размера (сколько вершин)
        heap3 = DHeap(self.num_nodes, 3)
        heap3.keys[src] = 0
        heap3.buildHeap()

        # Пока куча не пуста
        while not heap3.isEmpty():
            # Извлекаем минимальную по расстоянию вершину u
            key, u = heap3.extractMin()
            self.dist[u] = key

            # Обходим все вершины v, из которых можно перейти из u
            for v, w in self.adjList[u]:
                # Если вершины v уже нет в куче - пропускаем её
                if v not in heap3.pos:
                    continue

                # Вершина v находится в куче.
                # Затем расстояние до неё обновляется, если
                # расстояние от src до u + от u до v меньше,
                # чем текущее общее от src до v
                idx = heap3.pos[v]
                newDist = self.dist[u] + w
                if heap3.keys[idx] > newDist:
                    heap3.keys[idx] = newDist
                    heap3.bubbleUp(idx)

    # Запуск алгоритма Дейкстры на метках (из вершины src)
    def dijkstraMark(self, src):
        # Массив меток. h[i] = 0,
        # если построение кратчайшего пути из src в i не завершено; 1 - иначе
        h = [0] * self.num_nodes

        # До всех вершин назначаются расстояния от исходной как +бесконечность
        for u in self.adjList.keys():
            self.dist[u] = maxsize
        # (кроме вершины, из которой алгоритм начинает работу)
        self.dist[src] = 0

        # Пройдём n (n = num_nodes) раз, то есть каждую вершину, и каждый раз...
        for _ in range(self.num_nodes):
            # Находим индекс c первой вершины, кратчайшее расстояние до которой
            # ещё не известно
            c = 0
            while h[c] != 0:
                c = c + 1

            # Далее из всех вершин, находящихся в h не до с,
            # для которых ещё не известно кратчайшее расстояние,
            # находим такую вершину i, расстояние до которой меньше всех других
            i = c
            for k in range(c + 1, self.num_nodes):
                if h[k] == 0:
                    if self.dist[k] < self.dist[i]:
                        i = k

            # Указываем, что теперь знаем кратчайшее расстояние до вершины i
            h[i] = 1

            # И рассматриваем все вершины j, смежные с i
            # (то есть те, в которые можно перейти из i)

            for p in self.adjList[i]:
                j = p[0]
                w = p[1]

                # Если до вершины j ещё не было найдено кратчайшего расстояния,
                if h[j] == 0:
                    # и текущее расстояние до j > расстояния до i + вес ребра i->j,
                    # то обновим расстояние на новое (меньшее)
                    if self.dist[j] > self.dist[i] + w:
                        self.dist[j] = self.dist[i] + w
