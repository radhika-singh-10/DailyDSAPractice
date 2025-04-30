class UnionFind:
    def __init__(self,n:int):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]]
        return self.parent[x]
    
    def union(self,x,y):
        component_x,component_y=self.find(x),self.find(y)
        if component_x==component_y:
            return 
        if self.rank[component_x]<self.rank[component_y]:
            self.parent[component_x]=y
        else:
            self.parent[component_y]=x
            if self.parent[component_x]==self.parent[component_y]:
                self.rank[component_x]+=1
        

    
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        # m=len(queries)
        # res=[False]*m
        # for i in range(m):
        #     x,y=queries[i][0],queries[i][1]
        #     res[i]=True if abs(nums[x]-nums[y])<=maxDiff else False
        #     #print(abs(nums[x]-nums[y]),maxDiff,abs(nums[x]-nums[y])<=maxDiff)
        # #for connected components finding we eneed to apply union find
        
        # return res

        #for connected components finding we eneed to apply union find
        uf=UnionFind(n)
        for (u,nu), (v,nv) in pairwise(enumerate(nums)):
            if nv-nu<=maxDiff:
                uf.union(u,v)
        return [uf.find(u)==uf.find(v) for u,v in queries]

