class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        m,n=len(matrix),len(matrix[0])
        for row,col in zip(matrix,zip(*matrix)):
            if len(set(row))!=n or len(set(col))!=m:
                return False
                
        return True 