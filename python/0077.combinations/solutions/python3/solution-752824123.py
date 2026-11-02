# leetcode.cn/problems/combinations/  (77)
# submission 752824123  accepted 2026-10-04  runtime 111 ms  memory 60.1 MB

class Solution:
    n: int
    k: int
    res: list[list[int]]
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.n = n
        self.k = k
        self.res = []
        self._dfs([], 1)

        return self.res



    def _dfs(self, lst: list[int], start: int):
        if len(lst) == self.k:
            self.res.append(lst.copy())
            return
        
        for i in range(start, self.n + 1):
            lst.append(i)
            self._dfs(lst, i + 1)
            lst.pop()
