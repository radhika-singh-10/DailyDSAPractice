import random

class RandomizedSet:

    def __init__(self):
        self.ls = []  # List to store elements
        self.hm = {}  # Dictionary to store element indices

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        self.ls.append(val)
        self.hm[val] = len(self.ls) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False
        idx = self.hm[val]
        last_el = self.ls[-1]
        self.ls[idx] = last_el
        self.hm[last_el] = idx
        self.ls.pop()
        del self.hm[val]
        
        return True

    def getRandom(self) -> int:
        loc = random.randint(0, len(self.ls) - 1)
        return self.ls[loc]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()