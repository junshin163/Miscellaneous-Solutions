class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        D = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        
        cache = {}
        
        def combo(digits):
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return D[digits[0]]
            if len(digits) not in cache:
                prevCombo = combo(digits[0:len(digits)-1])
                result = []
                for i in range(len(D[digits[-1]] )):
                    for j in range(len(prevCombo)):
                        result.append(prevCombo[j] + D[digits[-1]][i])
                cache[len(digits)] = result 
            return cache[len(digits)]
        return combo(digits)
