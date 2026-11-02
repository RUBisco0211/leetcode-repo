// leetcode.cn/problems/ransom-note/  (383)
// submission 544206903  accepted 2024-07-05  runtime 14 ms  memory 11.1 MB

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
            if (map[ch] < 0)
                return false;
        }
        return true;
    }
};
