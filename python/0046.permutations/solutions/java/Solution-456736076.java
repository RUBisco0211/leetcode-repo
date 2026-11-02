// leetcode.cn/problems/permutations/  (46)
// submission 456736076  accepted 2023-08-15  runtime 1 ms  memory 42.2 MB

class Solution {
    public List<List<Integer>> permute(int[] nums){
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        boolean[] visited = new boolean[nums.length];
        dfs(nums, visited, result, new ArrayList<Integer>());
        return result;
    }
    private void dfs(int[] nums, boolean[] visited, List<List<Integer>> result, List<Integer> list){
        if(list.size() == nums.length){
            result.add(new ArrayList(list));
            return;
        }
        for(int i = 0; i < nums.length; i++){
            if(!visited[i]){
                visited[i] = true;
                list.add(nums[i]);
                dfs(nums, visited, result, list);
                visited[i] = false;
                list.remove(list.size() - 1);
            }
        }
    }
}
