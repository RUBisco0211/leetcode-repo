# leetcode.cn/problems/subsets/  (78)
# submission 752788711  accepted 2026-10-04  runtime 0 ms  memory 19.1 MB

class Solution:
    res: list[list[int]]
    nums: list[int]

    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.res = []
        self._dfs([], 0)

        return self.res
    
    def _dfs(self, lst: list[int], start: int):    
        self.res.append(lst.copy())
        for i in range(start, len(self.nums)):
            lst.append(self.nums[i])
            self._dfs(lst, i + 1)
            lst.pop()
