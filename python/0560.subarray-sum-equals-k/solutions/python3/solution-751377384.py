# leetcode.cn/problems/subarray-sum-equals-k/  (560)
# submission 751377384  accepted 2026-09-25  runtime 31 ms  memory 21.7 MB

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return (1 if nums[0] == k else 0)

        res = 0
        pre = 0
        mp = {
            0: 1
        }

        for i, n in enumerate(nums):
            pre += n
            if pre - k in mp:
                res += mp[pre - k]
            if pre in mp:
                mp[pre] += 1
            else:
                mp[pre] = 1

        return res
