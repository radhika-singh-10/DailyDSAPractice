from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #tik tok potential questions for oa round
        if not heights or not heights[0]:
            return []

        n, m = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(starts):
            visited = set()
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < n and 0 <= nc < m and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):
                        queue.append((nr, nc))
            return visited

        pacific_starts = [(0, j) for j in range(m)] + [(i, 0) for i in range(n)]
        atlantic_starts = [(n - 1, j) for j in range(m)] + [(i, m - 1) for i in range(n)]

        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)

        return list(pacific_reachable & atlantic_reachable)

