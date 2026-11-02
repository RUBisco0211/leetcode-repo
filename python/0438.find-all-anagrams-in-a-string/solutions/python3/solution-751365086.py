# leetcode.cn/problems/find-all-anagrams-in-a-string/  (438)
# submission 751365086  accepted 2026-09-25  runtime 7562 ms  memory 19.6 MB

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return res
        
        sp = ''.join(sorted(p))
        for start in range(0, ls - lp + 1):
            subs = s[start: start + lp]
            ss = ''.join(sorted(subs))
            if sp == ss:
                res.append(start)
        
        return res
