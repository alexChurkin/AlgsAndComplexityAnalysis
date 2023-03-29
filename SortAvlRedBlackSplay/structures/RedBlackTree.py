from structures.Stack import Stack


class RBNode(object):
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.red = False

    def print(self):
        self.__printRec(self)

    def __printRec(self, root, tabCount=0):
        if root is None:
            return

        for i in range(0, tabCount):
            print("  ", end='')

        print(str(root.key) + (", red" if root.red else ", black"))
        self.__printRec(root.left, tabCount + 1)
        self.__printRec(root.right, tabCount + 1)


class RedBlackIterator:
    def __init__(self, tree):
        self.pos = 0
        self.count = tree.count
        self.stack = Stack()

        self.currNode = tree.root

        while self.currNode is not None:
            self.stack.push(self.currNode)
            self.currNode = self.currNode.left

        if not self.stack.isEmpty():
            self.currNode = self.stack.peek()

        self.currNode = self.getNextNode()

    def __iter__(self):
        return self

    def getNextNode(self):
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

        if self.currNode.key is None:
            return None
        else:
            return self.currNode

    def __next__(self):
        if self.pos == self.count:
            raise StopIteration
        if self.pos == 0:
            self.pos += 1
            return self.currNode.key

        node = None
        while node is None:
            node = self.getNextNode()

        self.currNode = node
        self.pos += 1

        return self.currNode.key


class RedBlackTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
        self.count = 0

    def print(self):
        if self.root is None:
            return
        self.root.print()

    def insert(self, key):
        # Обычная вставка
        newNode = RBNode(key)
        newNode.parent = None
        newNode.left = self.nil
        newNode.right = self.nil
        # Новое звено должно быть красным
        newNode.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if newNode.key <= current.key:
                current = current.left
            else:
                current = current.right

        # Установка parent и вставка звена
        newNode.parent = parent
        if parent is None:
            self.root = newNode
        elif newNode.key <= parent.key:
            parent.left = newNode
        else:
            parent.right = newNode

        # Исправление дерева
        self.fix_insert(newNode)

        self.count += 1

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # "дядя"
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.left_rotate(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # "дядя"

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.right_rotate(new_node.parent.parent)
        self.root.red = False

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
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

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
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

    def __iter__(self):
        return RedBlackIterator(self)
