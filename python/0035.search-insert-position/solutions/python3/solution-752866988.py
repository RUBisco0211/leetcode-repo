# leetcode.cn/problems/search-insert-position/  (35)
# submission 752866988  accepted 2026-10-05  runtime 0 ms  memory 19.9 MB

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
