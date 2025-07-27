class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        n,m = len(matrix),len(matrix[0])
        self.matrix=[[0]*(m+1) for _ in range(n)]
        for r in range(n):
            for c in range(m):
                self.matrix[r][c+1]=self.matrix[r][c]+matrix[r][c]        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=0
        for r in range(row1,row2+1):
            res+=self.matrix[r][col2+1]-self.matrix[r][col1]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)