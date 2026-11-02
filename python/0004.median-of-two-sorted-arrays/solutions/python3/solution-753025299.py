# leetcode.cn/problems/median-of-two-sorted-arrays/  (4)
# submission 753025299  accepted 2026-10-06  runtime 4 ms  memory 19.3 MB

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        merged = []
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        while i < n:
            merged.append(nums1[i])
            i += 1

        while j < m:
            merged.append(nums2[j])
            j += 1
        
        if (m + n) % 2 == 1:
            return merged[(m + n) // 2]
        else:
            return (merged[(m + n) // 2 - 1] + merged[(m + n) // 2]) / 2
