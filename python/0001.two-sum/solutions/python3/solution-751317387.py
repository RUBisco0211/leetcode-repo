# leetcode.cn/problems/two-sum/  (1)
# submission 751317387  accepted 2026-09-24  runtime 3 ms  memory 20.3 MB

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            rest = target - num
            if rest in num_dict:
                return [i, num_dict[rest]]

            num_dict[num] = i
        return []
