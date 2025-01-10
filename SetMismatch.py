class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[]
        s=set(nums)
        n=[]
        for i in range(1,len(nums)+1):
            n.append(i)
        for i in n:
            if i in s:
                nums.remove(i)
        ans.append(nums[0])
        for i in n:
            if i not in s :
                ans.append(i)
        return ans
