class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==0:
            return []
        elif n==1:
            return [[1]]
        
        prevRows=self.generate(n-1)
        prevRow=prevRows[-1]
        curRow=[1]
        
        for i in range(1,n-1):
            curRow.append(prevRow[i-1]+prevRow[i])
            #print(curRow,prevRow[i-1]+prevRow[i])
        
        curRow.append(1)
        prevRows.append(curRow)
        return prevRows