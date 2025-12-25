class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        m,n=len(rowCosts),len(colCosts)
        if startPos==homePos:
            return 0
        res=0
        if startPos[0]<homePos[0]:
            for row in range(startPos[0],homePos[0]):
                res+=rowCosts[row+1]
        else:
            for row in range(startPos[0],homePos[0],-1):
                res+=rowCosts[row-1]

        if startPos[1]<homePos[1]:
            for col in range(startPos[1],homePos[1]):
                res+=colCosts[col+1]
        else:
            for col in range(startPos[1],homePos[1],-1):
                res+=colCosts[col-1]
        return res

        

        
