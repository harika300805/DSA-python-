class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        l=0
        ans=0
        temp=0
        for r in range(len(arr)) :
            if arr[r] == 0 :
                temp+=1
            while temp > k :
                if arr[l] == 0:
                    temp-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
