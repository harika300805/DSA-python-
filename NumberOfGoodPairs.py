class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        temp,ans=0,0
        for j in d.values():
            temp=j*(j-1)//2
            ans += temp
        return ans

        
