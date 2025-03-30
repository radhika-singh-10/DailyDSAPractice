class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #same row-i, col-j, diagonal-i+j, antidiagonal-i-j
        #we will apply backtracking
        # grid=[['.']*n for _ in range(n)]
        res=[]
        def backtrackCheck(row,rowSet,colSet,diagonalSet,antiDiagonalSet,board):
            if row==n:
                res.append(board)
            for col in range(n):
                
                isValidRowCol=(row not in rowSet) and (col not in colSet) and (row+col not in diagonalSet) and (row-col not in antiDiagonalSet)

                if isValidRowCol:
                    backtrackCheck(row+1,rowSet.union({row}),colSet.union({col}),diagonalSet.union({row+col}),antiDiagonalSet.union({row-col}),board+['.'*col+'Q'+'.'*(n-col-1)])

                


        backtrackCheck(0,set(),set(),set(),set(),[])
        return res




