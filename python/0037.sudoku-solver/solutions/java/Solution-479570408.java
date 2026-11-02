// leetcode.cn/problems/sudoku-solver/  (37)
// submission 479570408  accepted 2023-11-03  runtime 6 ms  memory 38.7 MB

class Solution {
    public static void solveSudoku(char[][] board) {
        backTracking(board);
    }
    private static boolean backTracking(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.')
                    continue;
                for (char ch = '1'; ch <= '9'; ch++) {
                    if (isValid(board, i, j, ch)) {
                        board[i][j] = ch;
                        if (backTracking(board))
                            return true;
                    }
                    board[i][j] = '.';
                }
                return false;
            }
        }
        return true;
    }
    private static boolean isValid(char[][] board, int row, int col, char ch) {
        for (int j = 0; j < 9; j++) {
            if (board[row][j] == ch)
                return false;
        }
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == ch)
                return false;
        }
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for (int i = startRow; i < startRow + 3; i++) {
            for (int j = startCol; j < startCol + 3; j++) {
                if (board[i][j] == ch)
                    return false;
            }
        }
        return true;
    }
}
