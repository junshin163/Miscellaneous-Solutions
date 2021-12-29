class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                s = nums[i] + nums[j]
                lo, hi = j + 1, len(nums) - 1
                while lo < hi:
                    if s + nums[lo] + nums[hi] > target:
                        hi -= 1
                    elif s + nums[lo] + nums[hi] < target:
                        lo += 1
                    elif s + nums[lo] + nums[hi] == target:
                        res.append([nums[i], nums[j], nums[lo], nums[hi] ])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1
                j += 1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
        return res
