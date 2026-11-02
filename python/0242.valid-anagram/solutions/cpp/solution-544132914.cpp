// leetcode.cn/problems/valid-anagram/  (242)
// submission 544132914  accepted 2024-07-04  runtime 4 ms  memory 8.4 MB

class Solution {
public:
    bool isAnagram(std::string s, std::string t)
    {
        int hashmap[26] = {0};
        for (char ch : s)
            hashmap[ch - 'a']++;
        for (char ch : t)
            hashmap[ch - 'a']--;
        for (int i = 0; i < 26; i++)
        {
            if (hashmap[i] != 0)
            {
                return false;
            }
        }
        return true;
    }
};
