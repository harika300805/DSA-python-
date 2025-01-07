class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        low=nums[0]
        for i in range(1,n):
            if nums[i]>low:
                res=nums[i]-low
                ans=max(ans,res)
            else:
                low=min(low,nums[i])
        if ans != 0:
            return ans
        else:
            return -1
