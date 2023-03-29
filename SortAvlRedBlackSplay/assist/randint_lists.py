import random


def generateRandomList(size: int, minimum: int, maximum: int) -> list:
    randList = [random.randint(minimum, maximum) for i in range(size)]
    return randList


def generateRandomListAsc(size: int, minimum: int, maximum: int) -> list:
    randList = generateRandomList(size, minimum, maximum)
    randList.sort()
    return randList


def generateRandomListDesc(size: int, minimum: int, maximum: int) -> list:
    randList = generateRandomList(size, minimum, maximum)
    randList.sort(reverse=True)
    return randList
