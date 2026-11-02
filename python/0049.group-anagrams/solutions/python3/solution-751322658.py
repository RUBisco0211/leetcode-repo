# leetcode.cn/problems/group-anagrams/  (49)
# submission 751322658  accepted 2026-09-24  runtime 15 ms  memory 21.7 MB

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        tmp = {}
        for s in strs:
            key = s if len(s) <= 1 else ''.join(sorted(s))
                
            if key in tmp:
                tmp[key].append(s)
                continue
            tmp[key] = [s]
        return list(tmp.values())
