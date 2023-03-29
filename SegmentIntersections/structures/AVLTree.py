from structures.AVLNode import AVLNode

"""
AVL-дерево
"""


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVLTree(object):
    """
    Реализация AVL-дерева.
    """

    def __init__(self):
        """ Дерево пусто """
        self.root = None

    def print(self):
        if self.root is None:
            return
        self.root.print()

    def find(self, k):
        """
        Находит и возвращает звено с ключом k в поддереве с корнем self.

        Принимает:
            k: Ключ звена, которое нужно найти.
        Возвращает:
            Звено с ключом k или None, если не удалось найти.
        """
        return self.root and self.root.find(k)

    def find_min(self):
        """Возвращает звено с минимальным ключом в AVL-дереве."""
        return self.root and self.root.find_min()

    def next_larger(self, k):
        """
        Возвращает звено, содержащее наименее больший (следующий) ключ в AVL-дереве
        по отношению ко звену с ключом k.

        Принимает:
            k: Ключ звена, для которого должно быть найдено следующее.

        Возвращает: следующее
        """
        node = self.find(k)
        return node and node.next_larger()

    def prev_smaller(self, k):
        """
        Возвращает звено, содержащее наименее меньший (предыдущий) ключ в AVL-дереве
        по отношению ко звену с ключом k.
        """
        node = self.find(k)
        return node and node.prev_smaller()

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
            # поднимаемся вверх от node (ведь на уровне node уже произведена балансировка)
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

    def delete(self, k):
        """
        Удаляет и возвращает звено с ключом k, если оно существует в AVL-дереве.
        AVL-версия гарантирует сбалансированность: h = O(log N).

        Принимает:
            k: Ключ звена, которое необходимо удалить.

        Возвращает:
            Удалённое звено с ключом k.
        """
        # найдём удаляемое звено
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            # (оно является корнем)
            # создадим псевдокорень с ключом 0
            pseudoRoot = AVLNode(None, 0)
            # прикрепим слева текущий корень
            pseudoRoot.left = self.root
            # назначим родителем текущего корня наш псевдокорень
            self.root.parent = pseudoRoot
            # запустим удаление текущего корня
            deleted = self.root.delete()
            # теперь корнем станет звено, на которое был сменён старый текущий корень
            self.root = pseudoRoot.left
            if self.root is not None:
                self.root.parent = None
        else:
            # (оно не является корнем) -> удалим его стандартным delete у звена
            deleted = node.delete()
        # node.parent является старым родителем node,
        # поэтому он - первый потенциально несбалансированный узел.
        # Сбалансируем его.
        self.rebalance(deleted.parent)
