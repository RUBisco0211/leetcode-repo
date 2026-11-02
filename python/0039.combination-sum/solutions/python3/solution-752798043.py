# leetcode.cn/problems/combination-sum/  (39)
# submission 752798043  accepted 2026-10-04  runtime 3 ms  memory 19.4 MB

class Solution:
    res: list[list[int]]
    candidates: list[int]
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.candidates = candidates
        self.res = []
        self._dfs([], 0, target)
        return self.res

    def _dfs(self, lst: list[int], start: int, target: int):
        if target == 0:
            self.res.append(lst.copy())
        
        for i in range(start, len(self.candidates)):
            num = self.candidates[i]
            if target < num:
                continue
            lst.append(num)
            # start 可以从自己（i）开始，但不能再选前面的了，否则组合重复
            self._dfs(lst, i, target - num)
            lst.pop()
