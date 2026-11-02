# leetcode.cn/problems/product-of-array-except-self/  (238)
# submission 751426567  accepted 2026-09-25  runtime 31 ms  memory 27.4 MB

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre_prod = [1] * l
        suf_prod = [1] * l

        for i in range(1, l):
            pre_prod[i] = pre_prod[i - 1] * nums[i - 1]

        for i in range(l - 2, -1, -1):
            suf_prod[i] = suf_prod[i + 1] * nums[i + 1]
        
        return [p * s for p, s in zip(pre_prod, suf_prod)]
