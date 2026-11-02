# leetcode.cn/problems/decode-string/  (394)
# submission 752862310  accepted 2026-10-05  runtime 0 ms  memory 18.9 MB

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        repeat = 0
        res = ""

        for ch in s:
            match ch:
                case ch if '0' <= ch <= '9':
                    repeat = repeat * 10 + int(ch)
                case ch if 'a' <= ch <= 'z':
                    res += ch
                case '[':
                    stack.append((repeat, res))
                    repeat = 0
                    res = ""
                case ']':
                    last_rep, last_str = stack.pop()
                    res = last_str + last_rep * res
                    
        return res
