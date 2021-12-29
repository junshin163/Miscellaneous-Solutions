import random
class RandomizedSet(object):

    def __init__(self):
        self.dict = {}
        self.lst = []
        
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        indexToRemove = self.dict[val]
        lastInLst = self.lst[-1]
        self.lst[indexToRemove] = lastInLst
        self.dict[lastInLst] = indexToRemove
        self.lst.pop()
        self.dict.pop(val)
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
