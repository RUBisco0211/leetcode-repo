# leetcode.cn/problems/merge-intervals/  (56)
# submission 751419715  accepted 2026-09-25  runtime 8 ms  memory 21.9 MB

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        l = len(intervals)
        intervals.sort(key=lambda p : p[0])
        res = [intervals[0]]

        for i in range(1, l):
            last_start, last_end = res[-1]
            curr_start, curr_end = intervals[i]
            # 无重叠，直接放进结果
            if curr_start > last_end:
                res.append(intervals[i])
                continue
            # 有重叠，取二者的较大终点为新的终点，
            res[-1] = [last_start, max(last_end, curr_end)]

        return res
