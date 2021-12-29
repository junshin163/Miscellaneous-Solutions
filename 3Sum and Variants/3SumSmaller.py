class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #O(n^2):
        res = 0
        nums.sort()
        for i in range(len(nums)):
            lo , hi = i + 1, len(nums) - 1
            while lo < hi < len(nums):
                s = nums[lo] + nums[hi] + nums[i]
                if s < target:
                    res += (hi - lo)
                    lo += 1
                elif s >= target:
                    hi -= 1
        return res
