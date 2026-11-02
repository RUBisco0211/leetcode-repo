# leetcode.cn/problems/trapping-rain-water/  (42)
# submission 751346125  accepted 2026-09-25  runtime 19 ms  memory 20.8 MB

class Solution:
    def trap(self, height: list[int]) -> int:
        res = 0
        l = len(height)
        highest_left = [0] * l
        highest_right = [0] * l

        for i in range(1, l):
            highest_left[i] = max(highest_left[i - 1], height[i - 1])
        for i in range(l - 2, -1, -1):
            highest_right[i] = max(highest_right[i + 1], height[i + 1])

        for i in range(1, len(height) - 1):    
            h = min(highest_left[i], highest_right[i])
            if h > height[i]:
                res += h - height[i]
            
        return res
