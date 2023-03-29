from structures.Stack import Stack

""" AVL-дерево """


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVLNode(object):
    """ Звено AVL-дерева."""

    def __init__(self, parent, k):
        """
        Создаёт звено.

        Принимает:
            parent: Родительское звено.
            k: Ключ звена.
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def print(self):
        self.__printRec(self)

    def __printRec(self, root, tabCount=0):
        if root is None:
            return

        for i in range(0, tabCount):
            print("  ", end='')

        print(root.key)
        self.__printRec(root.left, tabCount + 1)
        self.__printRec(root.right, tabCount + 1)

    def insert(self, node):
        """
        Производит вставку звена в поддерево с корнем self.

        Принимает:
            node: Звено для вставки.
        """
        if node is None:
            # Вставить звено некуда
            return
        if node.key <= self.key:
            # Ключ вставляемого звена меньше текущего ключа
            if self.left is None:
                # Слева пусто - можно присоединить новое звено
                node.parent = self
                self.left = node
            else:
                # Слева не пусто - идём влево вниз и ищем место вставки дальше
                self.left.insert(node)
        else:
            # Ключ вставляемого звена больше текущего ключа
            if self.right is None:
                # Справа пусто - можно присоединить новое звено
                node.parent = self
                self.right = node
            else:
                # Справа не пусто - идём вправо вниз и ищем место вставки дальше
                self.right.insert(node)


class AVLIterator:
    def __init__(self, avlTree):
        self.pos = 0
        self.count = avlTree.count
        self.stack = Stack()

        self.currNode = avlTree.root
        while self.currNode is not None:
            self.stack.push(self.currNode)
            self.currNode = self.currNode.left

        if not self.stack.isEmpty():
            self.currNode = self.stack.peek()

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == self.count:
            raise StopIteration
        if self.pos == 0:
            self.pos += 1
            return self.currNode.key

        node = self.stack.pop()

        if self.currNode.right is not None:
            self.currNode = self.currNode.right
            while self.currNode is not None:
                self.stack.push(self.currNode)
                self.currNode = self.currNode.left
            self.currNode = self.stack.peek()
        else:
            if self.stack.size() == 0:
                self.currNode = node.right
            else:
                self.currNode = self.stack.peek()

        self.pos += 1

        return self.currNode.key


class AVLTree(object):
    """
    Реализация AVL-дерева.
    """

    def __init__(self):
        """ Дерево пусто """
        self.root = None
        self.count = 0

    def print(self):
        if self.root is None:
            return
        self.root.print()

    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def rebalance(self, node):
        # пока node - звено, а не None
        while node is not None:
            # пересчитаем его высоту
            update_height(node)
            # если слева перевес
            if height(node.left) >= 2 + height(node.right):
                # если у левого дочернего высота его левого дочернего >= высоты его правого дочернего
                if height(node.left.left) >= height(node.left.right):
                    # проводится правое вращение для node
                    self.right_rotate(node)
                else:
                    # иначе сначала проводится левое вращение для левого дочернего
                    self.left_rotate(node.left)
                    # а затем правое вращение для node
                    self.right_rotate(node)
            # если справа перевес
            elif height(node.right) >= 2 + height(node.left):
                # если у правого дочернего высота его правого дочернего >= высоты его левого дочернего
                if height(node.right.right) >= height(node.right.left):
                    # проводится левое вращение
                    self.left_rotate(node)
                else:
                    # иначе сначала проводится правое вращение для правого дочернего
                    self.right_rotate(node.right)
                    # а затем левое вращение для node
                    self.left_rotate(node)
            # поднимаемся от node (ведь на уровне node уже произведена балансировка)
            node = node.parent

    def insert(self, k):
        """
        Производит вставку звена с ключом k в поддерево с корнем self.
        AVL-версия гарантирует сбалансированность: h = O(log N).

        Принимает:
            k: Ключ звена, которое необходимо вставить.
        """
        node = AVLNode(None, k)
        if self.root is None:
            # Корень родителя None.
            self.root = node
        else:
            self.root.insert(node)
        self.rebalance(node)

        self.count += 1

    def __iter__(self):
        return AVLIterator(self)
