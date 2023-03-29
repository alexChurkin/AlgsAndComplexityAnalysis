from structures.AVLTree import AVLTree
from structures.RedBlackTree import RedBlackTree
from structures.SplayTree import SplayTree


def avlSort(inputList: list) -> list:
    tree = AVLTree()

    for item in inputList:
        tree.insert(item)

    return [element for element in tree]


def redBlackSort(inputList: list) -> list:
    tree = RedBlackTree()

    for item in inputList:
        tree.insert(item)

    return [element for element in tree]


def splaySort(inputList: list) -> list:
    tree = SplayTree()

    for item in inputList:
        tree.insert(item)

    return [element for element in tree]
