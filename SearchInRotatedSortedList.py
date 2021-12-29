class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] < nums[high]:  #no rotation
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:  #3 more cases
                if nums[low] <= nums[mid] and nums[high] < nums[mid]:
                    if target >= nums[low] and target <= nums[mid]:
                        high = mid - 1
                    elif target >= nums[mid] or target <= nums[high]:
                        low = mid + 1
                    else:
                        return -1
                elif nums[low] >= nums[mid]:
                    if  target <= nums[mid] or target >= nums[low]:
                        high = mid - 1
                    elif target >= nums[mid] and target <= nums[low]:
                        low = mid + 1
                    else:
                        return -1
        if low == high and nums[low] == target:
            return low
        return -1              
                    
'''nums[low]  ...   nums[mid]  ...  nums[high]'''
