class Stack(object):
    def __init__(self):
        self.stack: list = []

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, item) -> None:
        """Кладёт новый элемент на вершину стека."""
        self.stack.append(item)

    def pop(self):
        """Возвращает (и извлекает) один элемент с вершины стека."""
        if not self.stack:
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        """Возвращает (без извлечения) один элемент с вершины стека."""
        if not self.stack:
            raise Exception("Stack is empty")
        return self.stack[-1]

    def isEmpty(self) -> bool:
        """Проверяет, пуст ли стек."""
        return not bool(self.stack)

    def size(self) -> int:
        """Возвращает размер стека."""
        return len(self.stack)

    def __contains__(self, item) -> bool:
        """Проверяет, есть ли элемент в стеке"""
        return item in self.stack
