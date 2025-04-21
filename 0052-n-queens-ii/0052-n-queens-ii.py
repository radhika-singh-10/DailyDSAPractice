class Solution:
    def totalNQueens(self, n: int) -> int:
        res=0
        def backtrack(row,rowSet,colSet,diagonalSet,antiDiagonalSet):
            nonlocal res
            if row==n:
                res+=1
            for col in range(n):
                isValidCol = (row not in rowSet) and (col not in colSet) and (row+col not in diagonalSet) and (row-col not in antiDiagonalSet)
                if isValidCol:
                    backtrack(row+1,rowSet.union({row}),colSet.union({col}),diagonalSet.union({row+col}),antiDiagonalSet.union({row-col}))
        backtrack(0,set(),set(),set(),set())
        
        return res

