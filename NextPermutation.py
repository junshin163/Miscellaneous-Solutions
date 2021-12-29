class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        curr_index = len(nums) - 1
        index_to_change = -1
        while curr_index > 0 and index_to_change == -1:
            if nums[curr_index - 1] < nums[curr_index]:
                index_to_change = curr_index - 1
            curr_index -= 1
        if index_to_change == -1:
            for i in range(0, (len(nums))//2):
                temp = nums[i]
                nums[i] = nums[len(nums)-i-1]
                nums[len(nums)-i-1] = temp
        else:
            index_of_smallest_larger = index_to_change+1
            for i in range(index_to_change+2, len(nums)):
                if nums[i] > nums[index_to_change]:
                    index_of_smallest_larger = i
            temp = nums[index_to_change]
            nums[index_to_change] = nums[index_of_smallest_larger]
            nums[index_of_smallest_larger] = temp
            
            for i in range(index_to_change+1, index_to_change + 1 + (len(nums)-index_to_change)//2 ):
                temp = nums[i]
                nums[i] = nums[len(nums)+index_to_change - i]
                nums[len(nums)+index_to_change - i] = temp
            
    
        #print(index_to_change)
            #0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
