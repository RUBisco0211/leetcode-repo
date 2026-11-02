// leetcode.cn/problems/implement-trie-prefix-tree/  (208)
// submission 638387482  accepted 2025-06-22  runtime 45 ms  memory 54.4 MB

#include <iostream>
#include <vector>
#include <string>
#define LETTERCOUNT 26

using namespace std;

class TrieNode
{
public:
    TrieNode(bool end = false) : children(vector<TrieNode *>(LETTERCOUNT)), isEnd(end) {}
    ~TrieNode()
    {
        for (TrieNode *child : children)
        {
            if (child != nullptr)
                delete child;
        }
        children.clear();
    }

    void insert(string word)
    {
        TrieNode *node = this;
        for (char ch : word)
        {
            ch -= 'a';
            if (node->children[ch] == nullptr)
                node->children[ch] = new TrieNode();
            node = node->children[ch];
        }
        node->isEnd = true;
    }

    bool search(string word)
    {
        TrieNode *node = searchPrefix(word);
        return node != nullptr && node->isEnd;
    }

    bool startsWith(string prefix)
    {
        return searchPrefix(prefix) != nullptr;
    }

    string find(string str)
    {
        TrieNode *node = this;
        string temp;
        for (char ch : str)
        {
            int index = ch - 'a';
            if (node->children[index] == nullptr)
                break;
            temp += ch;
            node = node->children[index];
            if (node->isEnd)
                break;
        }
        return temp;
    }

private:
    vector<TrieNode *> children;
    bool isEnd;

    TrieNode *searchPrefix(string prefix)
    {
        TrieNode *node = this;
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

class Trie
{
public:
    Trie() : root(new TrieNode()) {}
    ~Trie() { delete root; }
    void insert(string word) { root->insert(word); }
    string find(string str) { return root->find(str); }
    bool search(string word) { return root->search(word); }
    bool startsWith(string prefix) { return root->startsWith(prefix); }

private:
    TrieNode *root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
