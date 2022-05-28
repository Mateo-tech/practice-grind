class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            MAX = max(MAX, sum)
        return MAX