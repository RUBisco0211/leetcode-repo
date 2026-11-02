# leetcode.cn/problems/permutations/  (46)
# submission 752784700  accepted 2026-10-04  runtime 0 ms  memory 19.4 MB

class Solution:
    res: list[list[int]]
    nums: list[int]
    visited: list[bool]
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.res = []
        self.nums = nums
        self.visited = [False] * len(nums) 

        self._dfs([])
        return self.res

    def _dfs(self, lst: list[int]):
        if len(lst) == len(self.nums):
            self.res.append(lst.copy())
            return
        for i, num in enumerate(self.nums):
            if self.visited[i]:
                continue
            self.visited[i] = True
            lst.append(num)
            self._dfs(lst)
            self.visited[i] = False
            lst.pop()
