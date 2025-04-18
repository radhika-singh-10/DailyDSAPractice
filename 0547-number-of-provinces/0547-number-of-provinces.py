from collections import deque,defaultdict

# class UnionFind:
#     def __init__(self,n):
#         self.par=list(range(n))
#         self.rank=[0]*n 

#     def find(self,a):
#         if self.par[a]!=a:
#             self.par[a]=self.find(self.par[a])
#         return self.par[a]

#     def union(self,a,b):
#         a_par=self.find(a)
#         b_par=self.find(b)
#         if self.rank[a_par]<self.rank[b_par]:
#             self.par[a_par]=b_par
#         elif self.rank[b_par]<self.rank[a_par]:
#             self.par[b_par]=a_par
#         else:
#             self.rank[a_par]=b_par
#             self.par[b_par]+=1

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # brute force solution
        # num=0
        # n=len(isConnected)
        # visited=[False]*n
        # graph=defaultdict(list)


        #we can union find method to get no of connected compontes 
        #find will look for nodes which will have same parent 
        #union will check and update the parent 
        n=len(isConnected)
        uf=UnionFind(n)
        count=n
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1 and uf.find(i)!=uf.find(j):
                    count-=1
                    uf.union(i,j)
        return count




        

        # for i in range(n):
        #     if not visited[i]:
        #         visited[i]=True
        #         num+=1
        #         queue=deque([i])
        #         while queue:
        #             node=queue.popleft()
        #             for i in range(len(isConnected)):
        #                 if isConnected[node][i]==1 and not visited[i]:
        #                     queue.append(i)
        #                     visited[i]=True

        # return num


