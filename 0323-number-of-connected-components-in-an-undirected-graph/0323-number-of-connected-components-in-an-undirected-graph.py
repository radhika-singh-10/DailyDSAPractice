class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
        self.count=n

    def find(self,a):
        if a!=self.parent[a]:
            self.parent[a]=self.find(self.parent[a])
        #return a
        return self.parent[a]

    def union(self,a,b):
        parent_a=self.find(a)
        parent_b=self.find(b)
        if parent_a!=parent_b:
            self.parent[parent_a]=parent_b
            self.count-=1
        return 

    def getCount(self):
        return self.count

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=n
        uf=UnionFind(n)
        for a,b in edges:
            uf.union(a,b)
        return uf.getCount()
