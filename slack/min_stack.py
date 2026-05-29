# Problem: Min Stack
# Pattern: Stack
# Time:
# push  -> O(1)
# pop   -> O(1)
# top   -> O(1)
# getMin-> O(1)

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:

        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(
                min(val, self.min_stack[-1])
            )

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":

    minStack = MinStack()

    minStack.push(1)
    minStack.push(2)
    minStack.push(0)

    print(minStack.getMin())  # 0

    minStack.pop()

    print(minStack.top())     # 2
    print(minStack.getMin())  # 1