class UnionFind:
    def __init__(self,n):
        self.parent=[-1]*n
        self.rank=[0]*n
        self.count=0
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootx,rooty=self.find(x),self.find(y)

        if rootx!=rooty:
            if self.rank[rootx]<self.rank[rooty]:
                self.parent[rootx]=rooty
            elif self.rank[rooty]<self.rank[rootx]:
                self.parent[rooty]=rootx
            else:
                self.parent[rootx]=rooty
                self.rank[rooty]+=1
            self.count-=1
        print(self.count,x,y,rootx,rooty)
    
    def add(self,x):
        if self.parent[x]==-1:
            self.parent[x]=x
            self.count+=1
    
    def getCount(self):
        return self.count

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        #union-find/disjoint set-> find- parent component, union-count the related components
        #it can be solved in klog(mn) -> if m*n -> converted r*n+c linear relation 
        res=[]
        neighbors=[[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited=set()

        uf = UnionFind(m*n)
        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n and uf.parent[r*n+c] != -1

        for r,c in positions:
            i=r*n+c
            uf.add(i)
            for dx,dy in neighbors:
                nr,nc=r+dx,c+dy
                if isValid(nr,nc):
                    uf.union(i,nr*n+nc)
            res.append(uf.count)
        return res
        







        

