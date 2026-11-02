# leetcode.cn/problems/climbing-stairs/  (70)
# submission 751682328  accepted 2026-09-27  runtime 0 ms  memory 19.1 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        pre, curr = 1, 2

        for _ in range(3, n + 1):
            tmp = curr
            curr = pre + tmp
            pre = tmp
        
        return curr
