# leetcode.cn/problems/rotate-array/  (189)
# submission 751420530  accepted 2026-09-25  runtime 25 ms  memory 34.9 MB

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        l = len(nums)
        if k >= l:
            k = k % l
        nums[:] = nums[l - k : l] + nums[0: l - k]
