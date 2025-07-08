class Solution:
    def generate(self, n: int) -> List[List[int]]:
        triangle = []

        for i in range(n):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[i - 1][j - 1] + triangle[i- 1][j]
            triangle.append(row)
        return triangle


        # if n==0:
        #     return []
        # elif n==1:
        #     return [[1]]
        
        # prevRows=self.generate(n-1)
        # prevRow=prevRows[-1]
        # curRow=[1]
        
        # for i in range(1,n-1):
        #     curRow.append(prevRow[i-1]+prevRow[i])
        #     #print(curRow,prevRow[i-1]+prevRow[i])
        
        # curRow.append(1)
        # prevRows.append(curRow)
        # return prevRows