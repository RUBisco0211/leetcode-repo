// leetcode.cn/problems/valid-anagram/  (242)
// submission 544135350  accepted 2024-07-05  runtime 8 ms  memory 9.6 MB

class Solution {
public:
    bool isAnagram(std::string s, std::string t)
    {
        std::unordered_map<char, int> hashmap(26);
        for (char ch : s)
            hashmap[ch]++;
        for (char ch : t)
            hashmap[ch]--;
        for (const auto &pair : hashmap)
        {
            if (pair.second != 0)
                return false;
        }
        return true;
    }
};
