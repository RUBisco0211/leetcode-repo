// leetcode.cn/problems/ransom-note/  (383)
// submission 544201323  accepted 2024-07-05  runtime 18 ms  memory 10.9 MB

class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine)
    {
        std::unordered_map<char, int> map(26);
        for (char ch : magazine)
        {
            map[ch]++;
        }
        for (char ch : ransomNote)
        {
            if (map.count(ch) == 0)
                return false;
            map[ch]--;
        }
        for (auto &iter : map)
        {
            if (iter.second < 0)
                return false;
        }
        return true;
    }
};
