class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        D = {}
        result = []
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in D:
                D[sorted_string] = [string]
            else:
                D[sorted_string].append(string)
        for key in D:
            result.append(D[key])
        return result
