# leetcode.cn/problems/letter-combinations-of-a-phone-number/  (17)
# submission 752798372  accepted 2026-10-04  runtime 0 ms  memory 19.2 MB

class Solution:
    NUM_LETTER_MAP = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    res: list[str]
    digits: str
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        self.res = []
        self.digits = digits
        self._dfs("")
        return self.res

    def _dfs(self, s: str):
        # 工作字符串和原数字串长度相同时结束
        if len(s) == len(self.digits):
            self.res.append(s)
            return
        # 工作字符串 s 的长度也正是下一个待处理数字的索引
        digit = self.digits[len(s)]
        for ch in self.NUM_LETTER_MAP[digit]:
            self._dfs(s + ch)
