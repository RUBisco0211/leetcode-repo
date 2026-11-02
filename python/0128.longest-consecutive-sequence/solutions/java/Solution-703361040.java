// leetcode.cn/problems/longest-consecutive-sequence/  (128)
// submission 703361040  accepted 2026-03-06  runtime 33 ms  memory 93.8 MB

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i : nums) {
            set.add(i);
        }
        int max = 0;
        for (int i : set) {
            if (set.contains(i - 1)) {
                continue;
            }
            int next = i + 1;
            while (set.contains(next)) {
                next++;
            }
            max = Math.max(max, next - i);
        }

        return max;
    }
}
