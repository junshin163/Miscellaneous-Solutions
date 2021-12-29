class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.D = {}
        for word in dictionary:
            if len(word) == 1 or len(word) == 2:
                abbr = word
            else:
                abbr = word[0] + str( len(word)-2) + word[-1]
            if abbr not in self.D:
                self.D[abbr] = [word]
            else:
                self.D[abbr].append(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = word[0] + str( len(word)-2) + word[len(word)-1]
        if abbr not in self.D:
            return True
        if abbr in self.D and len(self.D[abbr]) == 1 and self.D[abbr][0] == word:
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
