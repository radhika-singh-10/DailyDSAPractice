class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m=len(matrix),len(matrix[0])
        # for i in range(n):
        #     for j in range(m):
        #         matrix[i][j],matrix[j][m-i-1]=matrix[j][m-i-1],matrix[i][j]
        for i in range(n):
            for j in range(i,m):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(n):
            l,r=0,n-1
            while l<r:
                matrix[i][l],matrix[i][r]=matrix[i][r],matrix[i][l]
                l+=1
                r-=1

                