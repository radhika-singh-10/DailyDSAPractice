class Solution:
    def totalNQueens(self, n: int) -> int:
        res=[]
        def backtrack(row,rowSet,colSet,diagonalSet,antiDiagonalSet,board):
            if row==n:
                res.append(board)
            for col in range(n):
                isValidCol = (row not in rowSet) and (col not in colSet) and (row+col not in diagonalSet) and (row-col not in antiDiagonalSet)
                if isValidCol:
                    backtrack(row+1,rowSet.union({row}),colSet.union({col}),diagonalSet.union({row+col}),antiDiagonalSet.union({row-col}),board+['.'*col+'Q'+'.'*(n-col-1)])
        backtrack(0,set(),set(),set(),set(),[])
        
        return len(res)

