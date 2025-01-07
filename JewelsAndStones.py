class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
            d={}
            for i in stones:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
            ans=0
            for j in jewels:
                if j in stones:
                    ans += d[j]
            return ans
