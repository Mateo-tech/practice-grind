class Solution:
    def containsDuplicate(self, nums):
        set = set()
        for i in nums:
            if i in set:
                return True
            else:
                set.add(i)