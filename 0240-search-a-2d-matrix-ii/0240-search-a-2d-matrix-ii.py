class Solution:
    def binarySearch(self,matrix,target,s,isVertical):
        l,r=s,len(matrix[0])-1 if isVertical else len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if isVertical:
                if target > matrix[s][m]:
                    l=m+1
                elif target < matrix[s][m]:
                    r=m-1
                else:
                    return True
            else:
                if target > matrix[m][s]:
                    l=m+1
                elif target < matrix[m][s]:
                    r=m-1
                else:
                    return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search approach-optimal 
        #binary search - one on row, other on column 
        #we check if found in column then return true, else return false 
        #then check for horizontal with the same logic


        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m,n=len(matrix),len(matrix[0])
        # l,r=0,m*n-1
        for i in range(min(len(matrix), len(matrix[0]))):
            verticalFound = self.binarySearch(matrix, target, i, True)
            horizontalFound = self.binarySearch(matrix, target, i, False)
            if verticalFound or horizontalFound:
                return True
        return False
       