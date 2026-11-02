# leetcode.cn/problems/longest-consecutive-sequence/  (128)
# submission 751330028  accepted 2026-09-24  runtime 45 ms  memory 36.2 MB

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        num_set = set(nums)
        res = 0
        for n in num_set:
            if n - 1 in num_set:
                continue
            tmp = n + 1 
            
            while tmp in num_set:
                tmp += 1

            res = max(res, tmp - n)


        return res
