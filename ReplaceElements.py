class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        amax=arr[n-1]
        alist=[-1]
        for i in range(n-1,0,-1):
            amax=max(amax,arr[i])
            alist.append(amax)
        alist.reverse()
        return alist
        
        
        
