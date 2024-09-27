class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n,m=len(board),len(board[0])
        cols,rows,squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(n):
            for c in range(m):
                if board[r][c]==".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
