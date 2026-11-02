// leetcode.cn/problems/longest-common-prefix/  (14)
// submission 541063355  accepted 2024-06-21  runtime 3 ms  memory 11.6 MB

class Trie
{
public:
    Trie()
    {
        children = vector<Trie *>(26);
        isEnd = false;
    }

    void insert(string word)
    {
        Trie *node = this;
        for (char ch : word)
        {
            ch -= 'a';
            if (node->children[ch] == nullptr)
                node->children[ch] = new Trie();
            node = node->children[ch];
        }
        node->isEnd = true;
    }

    bool search(string word)
    {
        Trie *node = searchPrefix(word);
        return node != nullptr && node->isEnd;
    }

    bool startsWith(string prefix)
    {
        return searchPrefix(prefix) != nullptr;
    }

    string findCommonPrefix(string str)
    {
        Trie *node = this;
        string temp;
        for (char ch : str)
        {
            int index = ch - 'a';
            if (node->children[index] == nullptr)
                break;
            temp.push_back(ch);
            node = node->children[index];
            if (node->isEnd)
                break;
        }
        return temp;
    }

private:
    vector<Trie *> children;
    bool isEnd;

    Trie *searchPrefix(string prefix)
    {
        Trie *node = this;
        for (char ch : prefix)
        {
            ch -= 'a';
            if (node->children[ch] == nullptr)
                return nullptr;
            node = node->children[ch];
        }
        return node;
    }
};

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.size() == 0)
            return "";
        string res = strs[0];
        int len = strs[0].length();

        Trie *trie = new Trie();
        trie->insert(strs[0]);

        for (int i = 1; i < strs.size(); i++)
        {
            string prefix = trie->findCommonPrefix(strs[i]);
            if (prefix == "")
            {
                res = "";
                break;
            }
            if (prefix.length() < len)
            {
                len = prefix.length();
                res = prefix;
            }
        }
        return res;
    }
};
