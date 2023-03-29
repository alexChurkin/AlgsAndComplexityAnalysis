from sys import maxsize


# d-куча (универсальная реализация)
class DHeap:
    # Принимает размер и d (в нашей работе это всегда 3)
    # Изначально все значения (keys) в куче равны +бесконечность
    def __init__(self, size, d):
        self.size = size
        self.d = d

        self.keys = [maxsize] * self.size
        self.nodes = [i for i in range(self.size)]
        self.pos = {}

    # Проверяет, пуста ли куча
    def isEmpty(self):
        return self.size == 0

    # Операция извлечения минимального элемента из кучи
    def extractMin(self):
        key, node = self.keys[0], self.nodes[0]
        self.keys[0], self.nodes[0] = self.keys[self.size - 1], self.nodes[self.size - 1]
        self.keys[self.size - 1], self.nodes[self.size - 1] = key, node
        del self.pos[node]

        self.size -= 1
        if self.size > 0:
            self.bubbleDown(0)

        return key, node

    def buildHeap(self):
        for i in range(self.size - 1, -1, -1):
            self.bubbleDown(i)

    # Возвращает индекс первого дочернего звена
    # для звена с индексом i
    def __firstChild(self, i):
        idx = i * self.d + 1
        return idx if idx < self.size else -1

    # Возвращает индекс последнего дочернего звена
    # для звена с индексом i
    def __lastChild(self, i):
        idx = min(i * self.d + self.d, self.size - 1)
        return idx if self.__firstChild(i) != -1 else -1

    # Возвращает индекс родительского звена
    # для звена с индексом i
    # (// - целочисленное деление)
    def __parent(self, i):
        return (i - 1) // self.d

    # Возвращает минимальный дочерний элемент (по ключу)
    def __minChild(self, i):
        first = self.__firstChild(i)
        if first == -1:
            return i

        last = self.__lastChild(i)
        min_key = self.keys[first]
        smallest = first
        for j in range(first + 1, last + 1):
            if self.keys[j] < min_key:
                min_key = self.keys[j]
                smallest = j

        return smallest

    # Операция погружения элемента (для восстановления св-ва кучи)
    def bubbleDown(self, i):
        key, node = self.keys[i], self.nodes[i]
        child = self.__minChild(i)
        while child != i and key > self.keys[child]:
            self.keys[i], self.nodes[i] = self.keys[child], self.nodes[child]
            self.pos[self.nodes[i]] = i

            i = child
            child = self.__minChild(i)

        self.keys[i], self.nodes[i] = key, node
        self.pos[self.nodes[i]] = i

    # Операция всплытия элемента (для восстановления св-ва кучи)
    def bubbleUp(self, i):
        key, node = self.keys[i], self.nodes[i]
        par = self.__parent(i)
        while i != -1 and self.keys[par] > key:
            self.keys[i], self.nodes[i] = self.keys[par], self.nodes[par]
            self.pos[self.nodes[i]] = i

            i = par
            par = self.__parent(i)

        self.keys[i], self.nodes[i] = key, node
        self.pos[self.nodes[i]] = i
