class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min = sys.maxsize
        for num in self.stack:
            if num < min:
                min = num
        return min