// leetcode.cn/problems/valid-anagram/  (242)
// submission 544135140  accepted 2024-07-05  runtime 12 ms  memory 9.5 MB

class Solution {
public:
    bool isAnagram(std::string s, std::string t)
    {
        std::unordered_map<char, int> hashmap(26);
        for (int i = 0; i < 26; i++)
            hashmap.insert({'a' + i, 0});
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
