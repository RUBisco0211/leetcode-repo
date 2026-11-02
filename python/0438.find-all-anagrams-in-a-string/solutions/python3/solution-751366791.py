# leetcode.cn/problems/find-all-anagrams-in-a-string/  (438)
# submission 751366791  accepted 2026-09-25  runtime 35 ms  memory 19.6 MB

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return res
        
        pdict = {}
        for ch in p:
            if ch not in pdict:
                pdict[ch] = 1
            else:
                pdict[ch] += 1

        sdict = {}
        for end in range(0, ls):
            if s[end] not in sdict:
                sdict[s[end]] = 1
            else:
                sdict[s[end]] += 1

            start = end - lp + 1
            if start < 0: 
                continue
            if pdict == sdict:
                res.append(start)
            sdict[s[start]] -= 1
            if sdict[s[start]] == 0:
                del sdict[s[start]]
        return res
