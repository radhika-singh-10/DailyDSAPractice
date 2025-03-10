class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        n,m = len(board),len(board[0])
        deep_copy_board = [[board[r][c] for c in range(m)] for r in range(n)]
        for row in range(n):
            for col in range(m):
                live = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    if (0<=r<n) and (0<=c<m) and (deep_copy_board[r][c] == 1):
                        live+=1
                if deep_copy_board[row][col] == 1 and (live < 2 or live > 3):
                    board[row][col] = 0
                if deep_copy_board[row][col] == 0 and live == 3:
                    board[row][col] = 1