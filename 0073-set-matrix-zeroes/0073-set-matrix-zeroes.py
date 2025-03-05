from collections import deque
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue=deque()
        n,m=len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    queue.append([i,j])

        while queue:
            row,col=queue.popleft()
            matrix[row]=[0]*m
            for j in range(n):
                matrix[j][col]=0
        return matrix
        

            