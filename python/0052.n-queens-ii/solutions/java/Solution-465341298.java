// leetcode.cn/problems/n-queens-ii/  (52)
// submission 465341298  accepted 2023-09-12  runtime 2 ms  memory 37.9 MB

class Solution {
    private static int count;
    public static int totalNQueens(int n) {
        int[][] chessBoard = new int[n][n];
        count = 0;
        setQueenInRow(chessBoard, 0);
        return count;
    }
    private static void setQueenInRow(int[][] chessBoard, int row) {
        int queensNum = chessBoard.length;
        for (int col = 0; col < queensNum; col++) {
            if (isLegal(chessBoard, row, col)) {
                chessBoard[row][col] = 1;
                if (row != queensNum - 1)
                    setQueenInRow(chessBoard, row + 1);
                else
                    count++;
            }
            chessBoard[row][col] = 0;
        }
    }
    private static boolean isLegal(int[][] chessBoard, int row, int col) {
        int queensNum = chessBoard.length;
        for (int i = 0; i < row; i++)
            if (chessBoard[i][col] == 1)
                return false;
        for (int j = 0; j < col; j++)
            if (chessBoard[row][j] == 1)
                return false;
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
            if (chessBoard[i][j] == 1)
                return false;
        for (int i = row - 1, j = col + 1; i >= 0 && j < queensNum; i--, j++)
            if (chessBoard[i][j] == 1)
                return false;
        return true;
    }
}
