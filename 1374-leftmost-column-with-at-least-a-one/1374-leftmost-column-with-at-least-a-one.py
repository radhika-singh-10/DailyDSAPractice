# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [rows,cols]=binaryMatrix.dimensions()
        res=cols
        #binary search can be applied to check if 0 is present
        for r in range(rows):
            l,h=0,cols-1
            while l<h:
                m=l+(h-l)//2
                if binaryMatrix.get(r,m)==0:
                    l=m+1
                else:
                    h=m
            if binaryMatrix.get(r, l) == 1:
                res=min(l,res)
        return -1 if res==cols else res
