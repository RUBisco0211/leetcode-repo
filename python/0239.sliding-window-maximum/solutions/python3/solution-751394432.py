# leetcode.cn/problems/sliding-window-maximum/  (239)
# submission 751394432  accepted 2026-09-25  runtime 187 ms  memory 35.9 MB

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)

        # 双端队列维护窗口索引，大的在左侧
        q = deque() 
        res = [0] * (l - k + 1)

        for end, n in enumerate(nums):
            # 把队列里右侧比 n 小的都出队
            while q and nums[q[-1]] <= n:
                q.pop()
            # 元素右侧入队，此时队列中已经按照大到小顺序排好
            q.append(end)

            left = end - k + 1
            # 窗口中的最大值位置（最左）已经在窗口左侧了，左侧出队
            if q[0] < left:
                q.popleft()
            # 记录窗口内最大值（队列最左侧） 
            if left >= 0:
                res[left] = nums[q[0]]
        
        return res
