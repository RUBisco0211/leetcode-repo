// leetcode.cn/problems/merge-intervals/  (56)
// submission 704916649  accepted 2026-03-09  runtime 11 ms  memory 48.2 MB

class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> res = new ArrayList<>();
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        if (intervals.length == 0)
            return null;
        res.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            int curStart = intervals[i][0], curEnd = intervals[i][1];
            int[] mergedLast = res.getLast();
//             当前区间起始比结果中最后一个区间的结束要早或相等，合并区间
            if (curStart <= mergedLast[1]) {
                int newEnd = Math.max(curEnd, mergedLast[1]);
                res.set(res.size() - 1, new int[]{mergedLast[0], newEnd});
            }
//            当前区间起始晚于结果中的最后一个区间结束，新的独立区间
            else {
                res.add(intervals[i]);
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}
