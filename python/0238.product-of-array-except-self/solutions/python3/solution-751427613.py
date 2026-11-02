# leetcode.cn/problems/product-of-array-except-self/  (238)
# submission 751427613  accepted 2026-09-25  runtime 24 ms  memory 25 MB

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        # suf_prod[i] 保存 i + 1 ~ l - 1 的乘积
        suf_prod = [1] * l

        for i in range(l - 2, -1, -1):
            suf_prod[i] = suf_prod[i + 1] * nums[i + 1]
        
        pre_prod = 1
        for i, n in enumerate(nums):
            # suf_prod[i] 距离答案就差 n 左侧的乘积了，即 pre_prod
            # suf_prod[i] 之后不会再用，可以直接覆盖掉作为答案
            suf_prod[i] *= pre_prod
            # pre_prod 累乘上当前数
            pre_prod *= n
        
        return suf_prod
