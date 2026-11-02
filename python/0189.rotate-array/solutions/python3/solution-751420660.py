# leetcode.cn/problems/rotate-array/  (189)
# submission 751420660  accepted 2026-09-25  runtime 31 ms  memory 34.6 MB

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        l = len(nums)
        if k >= l:
            k = k % l
        nums[:] = nums[-k:] + nums[0:-k]
