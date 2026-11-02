# leetcode.cn/problems/generate-parentheses/  (22)
# submission 752826119  accepted 2026-10-04  runtime 3 ms  memory 19.2 MB

class Solution:
    n: int
    res: list[str]
    def generateParenthesis(self, n: int) -> list[str]:
        self.n = n
        self.res = []
        path = [''] * (2 * n)
        self._dfs(path, 0, 0)

        return self.res

    def _dfs(self, path: list[str], left: int, right: int):
        # 合法的串的任何前缀中 ( 数量要大于等于 )，故 ( 最多是 n 个

        if right == self.n:
            self.res.append(''.join(path))
            return
        
        # ( 还没填完，可以填
        if left < self.n:
            path[left + right] = '('
            self._dfs(path, left + 1, right)
            path[left + right] = ''
        # ) 数量小于 (，可以填
        if right < left:
            path[left + right] = ')'
            self._dfs(path, left, right + 1)
            path[left + right] = ''
