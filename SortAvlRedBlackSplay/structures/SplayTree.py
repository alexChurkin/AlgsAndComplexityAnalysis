from structures.AVLTree import AVLIterator

""" Splay-дерево """


class SplayNode(object):
    """ Звено Splay-дерева."""

    def __init__(self, key):
        self.key = key
        self.parent = None
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


class SplayIterator(AVLIterator):
    def __init__(self, avlTree):
        super().__init__(avlTree)


class SplayTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def print(self):
        if self.root is None:
            return
        self.root.print()

    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def __splay(self, x):
        """
        Операция "Splay". Перемещает x в корень дерева
        """
        while x.parent is not None:
            if x.parent.parent is None:
                if x == x.parent.left:
                    # zig-поворот
                    self.__right_rotate(x.parent)
                else:
                    # zag-поворот
                    self.__left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zig-поворот
                self.__right_rotate(x.parent.parent)
                self.__right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag-поворот
                self.__left_rotate(x.parent.parent)
                self.__left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag-поворот
                self.__left_rotate(x.parent)
                self.__right_rotate(x.parent)
            else:
                # zag-zig-поворот
                self.__right_rotate(x.parent)
                self.__left_rotate(x.parent)

    def insert(self, key):
        """
        Производит вставку звена с ключом k в дерево.

        Принимает:
            key: Ключ звена, которое необходимо вставить.
        """
        node = SplayNode(key)
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.key <= x.key:
                x = x.left
            else:
                x = x.right

        # y - родитель x
        node.parent = y
        if y is None:
            self.root = node
        elif node.key <= y.key:
            y.left = node
        else:
            y.right = node
        # Проведём операцию "splay" для нового звена node
        self.__splay(node)
        self.count += 1

    def __iter__(self):
        return SplayIterator(self)
