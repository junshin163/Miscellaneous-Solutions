class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # two pointers:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i] != nums[i-1]:
                lo, hi = i+1, len(nums) - 1
                while lo < hi:
                    s = nums[lo] + nums[hi] + nums[i]
                    if s > 0:
                        hi -= 1
                    if s < 0:
                        lo += 1
                    if s == 0:
                        res.append([nums[lo], nums[hi], nums[i]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
        return res
