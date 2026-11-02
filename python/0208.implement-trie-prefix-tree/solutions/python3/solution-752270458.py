# leetcode.cn/problems/implement-trie-prefix-tree/  (208)
# submission 752270458  accepted 2026-09-30  runtime 139 ms  memory 53 MB

import string

class TrieNode:
    end: bool
    children: dict[str, 'TrieNode']

    def __init__(self, end: bool = False):
        self.end = end
        self.children = {ch: None for ch in string.ascii_lowercase}



class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if node.children[ch] is None:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def _searchPrefix(self, prefix: str) -> TrieNode | None:
        node = self.root
        for ch in prefix:
            if node.children[ch] is None:
                return None
            node = node.children[ch]
        return node
            
    def search(self, word: str) -> bool:
        node = self._searchPrefix(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        node = self._searchPrefix(prefix)
        return node is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
