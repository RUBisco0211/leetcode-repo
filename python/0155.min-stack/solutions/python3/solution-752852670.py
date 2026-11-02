# leetcode.cn/problems/min-stack/  (155)
# submission 752852670  accepted 2026-10-05  runtime 110 ms  memory 31.5 MB

class MinStack:
    st: list[int]

    def __init__(self):
        self.st = [(0, inf)]

    def push(self, value: int) -> None:
        m = min(value, self.st[-1][1])
        self.st.append((value, m))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
