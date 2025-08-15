"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        #divide and conquer
        #divide the matrix into 4 havles and check if same value in grid-isleaf, else further divide it it becomes a square of 4 size
        n=len(grid)
        if n == 1:
            return Node(val=bool(grid[0][0]), isLeaf=True)
        return self.recursion(grid,0,n,0,n)

    def recursion(self,grid,si,ei,sj,ej):
        val = grid[si][sj]
        node = Node(val==1,True)
        for i in range(si,ei):
            for j in range(sj,ej):
                if grid[i][j]!=val:
                    node.isLeaf=False
                    mi,mj=si+(ei-si)//2,sj+(ej-sj)//2
                    node.topLeft=self.recursion(grid,si,mi,sj,mj)
                    node.topRight=self.recursion(grid,si,mi,mj,ej)
                    node.bottomLeft=self.recursion(grid,mi,ei,sj,mj)
                    node.bottomRight=self.recursion(grid,mi,ei,mj,ej)
                    return node
        node.isLeaf,node.topLeft,node.topRight,node.bottomLeft,node.bottomRight=True,None,None,None,None
        return node



