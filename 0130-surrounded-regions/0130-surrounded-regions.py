class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m,n=len(board),len(board[0])
        #dirs=[[1,0],[0,1],[-1,0],[0,-1]]
        #apply dfs in recursive way
        if not board or not board[0]:
            return
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return 
            board[r][c] = '#'
            dfs(r-1,c) 
            dfs(r+1,c) 
            dfs(r,c-1) 
            dfs(r,c+1)


        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'