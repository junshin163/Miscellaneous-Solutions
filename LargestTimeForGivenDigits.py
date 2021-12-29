from itertools import permutations
class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        def isValidTime(string):
            if int(string[0:2]) > 23:
                return False
            if int(string[3:5]) > 59:
                return False
            return True
        
        def largerTime(t1, t2):
            if int(t1[0:2]) > int(t2[0:2]):
                return t1
            elif int(t1[0:2]) < int(t2[0:2]):
                return t2
            else:
                if int(t1[3:5]) < int(t2[3:5]):
                    return t2
                else:
                    return t1
        
        largestTime = ""
        for x in permutations(arr):
            timeStr = str(x[0]) + str(x[1]) + ":" + str(x[2]) + str(x[3])
            if isValidTime(timeStr):
                largestTime = timeStr
        for x in permutations(arr):
            timeStr = str(x[0]) + str(x[1]) + ":" + str(x[2]) + str(x[3])
            if isValidTime(timeStr):
                if largerTime(timeStr, largestTime) == timeStr:
                    largestTime = timeStr
        
        return largestTime
