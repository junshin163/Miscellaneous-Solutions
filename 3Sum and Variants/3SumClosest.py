class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        currClosest = 2 ** 31 - 1
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                lo, hi = i+1, len(nums)-1
                while lo < hi:
                    s = nums[lo] + nums[hi] + nums[i]
                    if abs(s - target) < abs(currClosest - target):
                        currClosest = s
                    if s > target:
                        hi -= 1
                    elif s < target:
                        lo += 1
                    else:
                        return target
        return currClosest
