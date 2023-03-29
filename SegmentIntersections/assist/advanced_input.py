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


"""..................... Вспомогательные функции ....................."""


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
