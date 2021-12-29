class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        #total O(3n^2) = O(n^2)
        D12, D34 = {}, {}
        # O(n^2)
        for num1 in nums1:
            for num2 in nums2:
                s12 = num1 + num2
                if s12 not in D12:
                    D12[s12] = 1
                else:
                    D12[s12] += 1
        
        # O(n^2)
        for num3 in nums3:
            for num4 in nums4:
                s34 = num3 + num4
                if s34 not in D34:
                    D34[s34] = 1
                else:
                    D34[s34] += 1
        
        count = 0
        # O(n^2)
        for key1 in D12:
            if -key1 in D34:
                count += (D12[key1] * D34[-key1])
        
        return count
