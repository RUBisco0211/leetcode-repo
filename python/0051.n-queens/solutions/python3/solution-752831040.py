# leetcode.cn/problems/n-queens/  (51)
# submission 752831040  accepted 2026-10-04  runtime 35 ms  memory 19.6 MB

class Solution:
    n: int
    res: list[list[str]]
    board: list[list[str]] # Q 为有皇后, . 为无
    def solveNQueens(self, n: int) -> list[list[str]]:
        self.n = n
        self.board = [['.'] * n for _ in range(n)]
        self.res = []
        self._setQueenInRow(0)

        return self.res

    def _setQueenInRow(self, row: int):
        for col in range(self.n):
            if self._isLegal(row, col):
                self.board[row][col] = 'Q'
                if row != self.n - 1:
                    self._setQueenInRow(row + 1)
                else:
                    snapshot = [''.join(row) for row in self.board]
                    self.res.append(snapshot)
            self.board[row][col] = '.'
    

    def _isLegal(self, row: int, col: int) -> bool:
        # 上方有其他皇后
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
        # 左侧有其他皇后
        for j in range(col):
            if self.board[row][j] == 'Q':
                return False
        # 左上斜线有其他皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 右上斜线有其他皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
