# leetcode.cn/problems/longest-substring-without-repeating-characters/  (3)
# submission 751362914  accepted 2026-09-25  runtime 255 ms  memory 19.7 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        start = 0
        res = 0
        for end in range(1, len(s)):
            subs = s[start: end]
            res = max(res, len(subs))
            ch = s[end]
            index = subs.find(ch)
            # 没找到重复字符，当前子串可以延续
            if index == -1:
                subs = s[start: end + 1]
                res = max(res, len(subs))
                continue
            # 找到重复字符，新子串跳到重复字符的后一位开始
            start += index + 1
        return res
