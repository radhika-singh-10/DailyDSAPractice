from collections import defaultdict, deque
# class UnionFind:
#     def __init__(self,N):
#         self.parent=list(range(N))
#     def find(self,x):
#         if self.parent[x]!=x:
#             self.parent[x]=self.find(self.parent[x])
#         return self.parent[x]
#     def union(self,x,y):
#         x,y=self.find(x),self.find(y)
#         if x==y:
#             return
#         if x>y:
#             self.parent[x]=y
#         else:
#             self.parent[y]=x
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #graph - undirected 
        # g=UnionFind(26)
        # n,m=len(s1),len(baseStr)
        # for i in range(n):
        #     g.union(ord(s1[i])-97,ord(s2[i])-97)
        # res=""
        # for i in baseStr:
        #     res+=(chr(g.find(ord(i)-97)+97))
        # return res

        if len(s1)!=len(s2):
            return ""
        equivGraph = defaultdict(set)
        for a,b in zip(s1,s2):
            equivGraph[a].add(a)
            equivGraph[a].add(b)
            equivGraph[b].add(b)
            equivGraph[b].add(a)
        #same with dfs
        smallestGraph = defaultdict(str)
        def searchMinChar(cur,minChar):
            if cur in smallestGraph:
                return 
            smallestGraph[cur]=minChar
            for eq in equivGraph[cur]:
                searchMinChar(eq,minChar)
        for c in [chr(ord('a')+i) for i in range(26)]:
            if c in equivGraph:
                if c in smallestGraph:
                    continue
                searchMinChar(c,c)
        return ''.join([smallestGraph[c] if c in smallestGraph else c for c in baseStr])



        


        
        
