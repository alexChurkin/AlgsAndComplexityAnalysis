"""............................ Основное ............................."""


def readInt(msg: str, minimum, maximum, includeL=True, includeR=True) -> int:
    k = None

    while not inRange(k, minimum, maximum, includeL, includeR):
        print(msg, end='')

        try:
            k = int(input())
            if not inRange(k, minimum, maximum, includeL, includeR):
                print(f"Некорректный ввод. Допустимый диапазон: "
                      f"{strRange(minimum, maximum, includeL, includeR)}")
        except ValueError:
            print(f"Некорректный ввод. Допустимый диапазон: "
                  f"{strRange(minimum, maximum, includeL, includeR)}")
            k = None
    return k


def readFloat(msg: str, minimum: float, maximum: float, includeL=True, includeR=True) -> float:
    k = None

    while not inRange(k, minimum, maximum, includeL, includeR):
        print(msg, end='')

        try:
            k = float(input())
            if not inRange(k, minimum, maximum, includeL, includeR):
                print(f"Некорректный ввод. Допустимый диапазон: "
                      f"{strRange(minimum, maximum, includeL, includeR)}")
        except ValueError:
            print(f"Некорректный ввод. Допустимый диапазон: "
                  f"{strRange(minimum, maximum, includeL, includeR)}")
            k = None
    return k


def readFloatRange(msg: str, minimum: float, maximum: float, includeL=True, includeR=True):
    a, b = None, None

    while not (inRange(a, minimum, maximum, includeL, includeR) and
               inRange(b, minimum, maximum, includeL, includeR) and
               a < b):
        print(msg, end='')

        try:
            inp = input().split(' ')
            a, b = float(inp[0]), float(inp[1])
            if not (inRange(a, minimum, maximum, includeL, includeR) and
                    inRange(b, minimum, maximum, includeL, includeR) and
                    a < b):
                print(f"Некорректный ввод. Нужно ввести 2 числа (a < b) через пробел. Допустимый диапазон: "
                      f"{strRange(minimum, maximum, includeL, includeR)}")
        except Exception:
            print(f"Некорректный ввод. Нужно ввести 2 числа через пробел. Допустимый диапазон: "
                  f"{strRange(minimum, maximum, includeL, includeR)}")
            a, b = None, None
    return a, b


def readFloatList(msg: str, minimum: float, maximum: float, includeL=True, includeR=True):
    _list = list()

    while not (len(_list) > 0 and
               floatListElementsInRange(_list, minimum, maximum, includeL, includeR)):
        try:
            _unformatted = input(msg).split(' ')

            if len(_unformatted) == 0:
                print(
                    f"Некорректный ввод. Нужно ввести числа через пробел. Допустимый диапазон: "
                    f"{strRange(minimum, maximum, includeL, includeR)}")

            _list = [float(elem) for elem in _unformatted]

            if not floatListElementsInRange(_list, minimum, maximum, includeL, includeR):
                print(
                    f"Некорректный ввод. Нужно ввести числа через пробел. Допустимый диапазон: "
                    f"{strRange(minimum, maximum, includeL, includeR)}")
        except Exception:
            print(
                f"Некорректный ввод. Нужно ввести числа через пробел. Допустимый диапазон: "
                f"{strRange(minimum, maximum, includeL, includeR)}")
            _list.clear()
    return _list


def listToStr(_list):
    result = ""

    if len(_list) <= 40:
        result += ''.join(str(_list))
    else:
        result += '['

        for i in range(15):
            result += str(_list[i])
            result += ', '
        result += '... , '

        for i in range(9):
            result += str(_list[len(_list) - 1 - i]) + ', '

        result += str(_list[len(_list) - 1]) + ']'

    return result


"""..................... Вспомогательные функции ....................."""


def floatListElementsInRange(listt, minimum, maximum, includeL: bool, includeR: bool):
    for element in listt:
        if not inRange(element, minimum, maximum, includeL, includeR):
            return False
    return True


def inRange(k, minimum, maximum, includeL: bool, includeR: bool):
    if includeL and includeR:
        return k is not None and minimum <= k <= maximum
    elif includeL:
        return k is not None and minimum <= k < maximum
    elif includeR:
        return k is not None and minimum < k <= maximum
    else:
        return k is not None and minimum < k < maximum


def strRange(minimum, maximum, includeL: bool, includeR: bool):
    s = ""
    s += ("[" if includeL else "(")
    s += f"{minimum}, {maximum}"
    s += ("]" if includeR else ")")
    return s
