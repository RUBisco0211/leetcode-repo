# leetcode.cn/problems/subsets/  (78)
# submission 752798845  accepted 2026-10-04  runtime 0 ms  memory 19.2 MB

class Solution:
    res: list[list[int]]
    nums: list[int]

    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.res = []
        self._dfs([], 0)

        return self.res
    
    def _dfs(self, lst: list[int], start: int):
        # 选到一个即可作为结果，无条件
        self.res.append(lst.copy())
        # nums[start:] 正是当前子集可选的元素集合，内部递归调用 start = i + 1 防止元素重复以及组合重复
        for i in range(start, len(self.nums)):
            lst.append(self.nums[i])
            self._dfs(lst, i + 1)
            lst.pop()
