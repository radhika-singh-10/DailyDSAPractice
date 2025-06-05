from collections import defaultdict, deque
class UnionFind:
    def __init__(self,N):
        self.parent=list(range(N))
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return
        if x>y:
            self.parent[x]=y
        else:
            self.parent[y]=x
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #graph - undirected 
        g=UnionFind(26)
        n,m=len(s1),len(baseStr)
        for i in range(n):
            g.union(ord(s1[i])-97,ord(s2[i])-97)
        res=""
        for i in baseStr:
            res+=(chr(g.find(ord(i)-97)+97))
        return res
        # n,m=len(s1),len(s2)
        # if n!=m:
        #     return ""
        # graph = defaultdict(set)
        # for a,b in zip(s1,s2):
        #     graph[a].add(a)
        #     graph[a].add(b)
        #     graph[b].add(b)
        #     graph[b].add(a)
        
        
