# leetcode.cn/problems/move-zeroes/  (283)
# submission 751342740  accepted 2026-09-25  runtime 4 ms  memory 20.3 MB

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
