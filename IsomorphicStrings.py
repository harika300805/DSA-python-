class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        r={}
        isIso = True
        for i in range(len(s)):
            if s[i] not in d and t[i] not in r:
                d[s[i]] = t[i]
                r[t[i]] = s[i]
            elif s[i] in d and d[s[i]] != t[i]:
                isIso=False
                break
            elif t[i] in r and r[t[i]] != s[i]:
                isIso=False
                break
        return isIso
