class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x:x[0])
        #union find
        uf=UnionFind(n)
        count=n
        for timestamp,a,b in logs:
            if uf.union(a,b):
                count-=1
            if count==1:
                return timestamp
        return -1
        
class UnionFind:

    def __init__(self,n):
        self.rank=[0]*n
        self.group=[group_id for group_id in range(n)]

    def find(self,a):
        if self.group[a]!=a:
            self.group[a]=self.find(self.group[a])
        return self.group[a]

    def union(self, a, b):
        
        groupA = self.find(a)
        groupB = self.find(b)
        if groupA == groupB:
            return False

        if self.rank[groupA] > self.rank[groupB]:
            self.group[groupB] = groupA
        elif self.rank[groupA] < self.rank[groupB]:
            self.group[groupA] = groupB
        else:
            self.group[groupA] = groupB
            self.rank[groupB] += 1

        return True

    