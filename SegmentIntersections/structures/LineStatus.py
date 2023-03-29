from structures.AVLTree import AVLTree


class LineStatus(object):
    """
        Класс-обёртка, представляющий состояние заметающей прямой.
        Его внутреннее AVL-дерево содержит все отрезки, пересечённые ею в данный момент.
    """

    def __init__(self):
        self.container = AVLTree()

    def insert(self, seg):
        self.container.insert(seg)

    def remove(self, seg):
        self.container.delete(seg)

    def adjSeg(self, seg):
        """
            Принимает: отрезок seg из статуса.
            Возвращает: прилегающие (верхний и нижний) отрезки.
        """
        nextSeg = self.container.next_larger(seg)
        prevSeg = self.container.prev_smaller(seg)

        if nextSeg is not None:
            nextSeg = nextSeg.key

        if prevSeg is not None:
            prevSeg = prevSeg.key

        return nextSeg, prevSeg

    def adjIntersections(self, seg):
        """
            Принимает: отрезок seg из статуса.
            Возвращает: (<есть ли пересечение с верхним отрезком>, <верхний отрезок>),
                        (<есть ли пересечение с нижним отрезком>, <нижний отрезок>)
        """
        nextSeg, prevSeg = self.adjSeg(seg)

        if nextSeg is not None:
            interNext = seg.intersects(nextSeg)
        else:
            interNext = False

        if prevSeg is not None:
            interPrev = seg.intersects(prevSeg)
        else:
            interPrev = False

        return (interPrev, prevSeg), (interNext, nextSeg)
