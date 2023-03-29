class AVLNode(object):
    """ Звено AVL-дерева."""

    def __init__(self, parent, k):
        """Создаёт звено.

        Принимает:
            parent: Родительское звено.
            k: Ключ звена.
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def print(self):
        self._printRec(self)

    def _printRec(self, root, tabCount=0):
        if root is None:
            return

        for i in range(0, tabCount):
            print("  ", end='')

        print(root.key, tabCount)
        self._printRec(root.left, tabCount + 1)
        self._printRec(root.right, tabCount + 1)

    def find(self, k):
        """
        Находит звено с ключом k в поддереве с корнем self.

        Принимает:
            k: Ключ звена, которое мы хотим отыскать.

        Возвращает:
            Звено с ключом k.
        """
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    def find_min(self):
        """
        Находит звено с минимальным ключом в поддереве с корнем self.

        Возвращает:
            Звено с минимальным ключом
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        """
        Находит звено с максимальным ключом в поддереве с корнем self.
        """
        current = self
        while current.right is not None:
            current = current.right
        return current

    def next_larger(self):
        """
        Находит в дереве звено с наименее большим (следующим) ключом.
        В терминах задаче о пересекающихся отрезках это "НАД".
        """
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def prev_smaller(self):
        """
        Находит в дереве звено с наименее меньшим (предыдущим) ключом.
        В терминах задаче о пересекающихся отрезках это "ПОД".
        """
        if self.left is not None:
            return self.left.find_max()
        current = self
        while current.parent is not None and current is current.parent.left:
            current = current.parent
        return current.parent

    def insert(self, node):
        """
        Производит вставку звена в поддерево с корнем self.

        Принимает:
            node: Звено для вставки.
        """

        if node is None:
            # Вставить звено некуда
            return
        if node.key < self.key:
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

    def delete(self):
        """Удаляет звено из дерева и возвращает его."""
        if self.left is None or self.right is None:
            # (если у self не более одного дочернего звена)

            if self is self.parent.left:
                # (self слева внизу от своего родителя)
                # заменим удаляемое звено на его единственное дочернее (если оно есть)
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    # если оно было, для заменённого звена нужно исправить ссылку на родителя
                    self.parent.left.parent = self.parent
            else:
                # (self справа внизу от своего родителя)
                # заменим удаляемое звено на его единственное дочернее (если оно есть)
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    # если оно было, для заменённого звена нужно исправить ссылку на родителя
                    self.parent.right.parent = self.parent
            return self
        else:
            # (если у self есть оба дочерних звена)

            # запустим поиск наименее большего (следующего)
            s = self.next_larger()
            # поменяем ключи текущего и наименее большего звеньев местами
            self.key, s.key = s.key, self.key
            # и запустим удаление уже для s
            return s.delete()
