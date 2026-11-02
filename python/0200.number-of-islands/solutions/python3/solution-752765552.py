# leetcode.cn/problems/number-of-islands/  (200)
# submission 752765552  accepted 2026-10-04  runtime 234 ms  memory 21.3 MB

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0

        def dfs(i: int, j: int):
            # 出界或不是陆地，则返回
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            # 标记了一处地点
            grid[i][j] = 'flaged'

            # 尝试标记周围的地块
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)


        for i in range(m):
            for j in range(n):
                # 找到一个新的陆地，标记它以及周围的地块，直到填满为止
                # 都填满之后，如果还有新的 '1' 那就是原来的旧陆地
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        
        return res
