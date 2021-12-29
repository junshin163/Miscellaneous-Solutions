class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if x >= 0:
            while x != 0:
                pop = x % 10
                x /= 10
                if (rev > (2 ** 31) /10 | (rev == (2 ** 31) / 10 & pop > 7)):
                    return 0
                if (rev < -(2 ** 31)/10 | (rev == -(2 ** 31) / 10 & pop < -8)):
                    return 0
                rev = rev * 10 + pop
            return rev
        else:
            x = -x
            while x != 0:
                pop = x % 10
                x /= 10
                if (rev > (2 ** 31) /10 | (rev == (2 ** 31) / 10 & pop > 7)):
                    return 0
                if (rev < -(2 ** 31)/10 | (rev == -(2 ** 31) / 10 & pop < -8)):
                    return 0
                rev = rev * 10 + pop
            return -rev
