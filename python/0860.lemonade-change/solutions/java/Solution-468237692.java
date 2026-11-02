// leetcode.cn/problems/lemonade-change/  (860)
// submission 468237692  accepted 2023-09-21  runtime 116 ms  memory 55.6 MB

class Solution {
    public static boolean lemonadeChange(int[] bills) {
        int fiveCount = 0, tenCount = 0;
        for (int bill: bills) {
            if (bill == 5)
                fiveCount++;
            if (bill == 10) {
                if (fiveCount > 0) {
                    tenCount++;
                    fiveCount--;
                } else
                    return false;
            }
            if (bill == 20) {
                if (tenCount > 0 && fiveCount > 0) {
                    tenCount--;
                    fiveCount--;
                } else if (fiveCount >= 3)
                    fiveCount -= 3;
                 else
                    return false;
            }
            System.out.println(String.valueOf(fiveCount) + '\t' + String.valueOf(tenCount));
        }
        return true;
    }
}
