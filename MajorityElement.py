class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mode = Counter(nums).most_common(1)[0][0]
        return mode
