class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        D = {}
        # O(n)
        for num in nums:
            if num not in D:
                D[num] = 1
            else:
                D[num] += 1
        D_rev = {}
        # O(n)
        for key in D:
            if D[key] not in D_rev:
                D_rev[ D[key] ] = [key]
            else:
                D_rev[ D[key] ].append(key)
        lst = []
        # O(n)
        for key in D_rev:
            lst.append(key)
        lst.sort()   # O(nlog n)
        lst.reverse()   # O(n)
        res = []
        for i in range(k):
            if len(res) < k:
                items_to_add = D_rev[lst[i]]
                for item in items_to_add:   # at most n items
                    res.append(item)
        return res
    
    # so final time complexity is O(nlog n)
