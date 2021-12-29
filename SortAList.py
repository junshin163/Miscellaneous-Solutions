# implementing merge sort
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        breakingPt = len(nums) // 2
        leftSorted = self.sortArray(nums[0:breakingPt])
        rightSorted = self.sortArray(nums[breakingPt:len(nums)])
        return self.merge(leftSorted, rightSorted)
        
        
        
    def merge(self, lst1, lst2):
        i, j = 0, 0
        mergedLst = []
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                mergedLst.append(lst1[i])
                i += 1
            else:
                mergedLst.append(lst2[j])
                j += 1
        if i < len(lst1):
            while i < len(lst1):
                mergedLst.append(lst1[i])
                i += 1
        if j < len(lst2):
            while j < len(lst2):
                mergedLst.append(lst2[j])
                j += 1
        return mergedLst
