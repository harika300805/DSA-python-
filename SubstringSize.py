class Solution:
    def countGoodSubstrings(self, li: str) -> int:
        c=0
        for i in range(len(li)-2):
            n=li[i:i+3]
            if len(n) == len(set(n)):
                c+=1
        return c
        
