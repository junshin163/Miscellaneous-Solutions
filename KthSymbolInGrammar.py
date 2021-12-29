class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def helper(n, k):
            if n == 1 or k == 1:
                return 0
            if k % 2 == 0:
                prev = helper(n-1, k/2)
                if prev == 0:
                    return 1
                else:
                    return 0
            else:
                prev = helper(n-1, (k+1)/2)
                if prev == 0:
                    return 0
                else:
                    return 1
        return helper(n, k)
