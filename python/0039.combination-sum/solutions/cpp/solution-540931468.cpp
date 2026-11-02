// leetcode.cn/problems/combination-sum/  (39)
// submission 540931468  accepted 2024-06-20  runtime 11 ms  memory 13.1 MB

class Solution {
public:
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        result = vector<vector<int>>{};
        sort(candidates.begin(), candidates.end());
        vector<int> list = vector<int>{};
        backTracking(candidates, 0, 0, target, list);
        return result;
    }

private:
    vector<vector<int>> result;
    void backTracking(vector<int>& candidates, int start, int sum, int target, vector<int>& list) {
        if (sum == target) {
            result.push_back(vector<int>(list));
            return;
        }
        if (sum > target) {
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            list.push_back(candidates[i]);
            backTracking(candidates, i, sum + candidates[i], target, list);
            list.pop_back();
        }
    }
};
