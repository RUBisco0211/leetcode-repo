// leetcode.cn/problems/n-queens/  (51)
// submission 465337895  accepted 2023-09-12  runtime 3 ms  memory 42.8 MB

class Solution {
    private static List<List<String>> result;
    public static List<List<String>> solveNQueens(int n) {
        int[][] chessBoard = new int[n][n];
        result = new ArrayList<>();
        setQueenInRow(chessBoard, 0);
        return result;
    }
    private static void setQueenInRow(int[][] chessBoard, int row) {
        int queensNum = chessBoard.length;
        for (int col = 0; col < queensNum; col++) {
            if (isLegal(chessBoard, row, col)) {
                chessBoard[row][col] = 1;
                if (row != queensNum - 1)
                    setQueenInRow(chessBoard, row + 1);
                else
                    addToResult(chessBoard);
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
    private static void addToResult(int[][] chessBoard) {
        List<String> board = new ArrayList<>();
        int queensNum = chessBoard.length;
        for (int i = 0; i < queensNum; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < queensNum; j++) {
                if (chessBoard[i][j] == 1)
                    sb.append('Q');
                else
                    sb.append('.');
            }
            board.add(sb.toString());
        }
        result.add(board);
    }
}
