class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        color_count = [[0] * 26 for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                color_count[i][ord(colors[i]) - ord('a')] = 1
        visited_nodes = 0
        max_color_val = 0
        while queue:
            node = queue.popleft()
            visited_nodes += 1
            max_color_val = max(max_color_val, max(color_count[node]))
            for neigbour in graph[node]:
                for c in range(26):
                    color_count[neigbour][c] = max(color_count[neigbour][c], color_count[node][c] + (1 if c == ord(colors[neigbour]) - ord('a') else 0))
                indegree[neigbour] -= 1
                if indegree[neigbour] == 0:
                    queue.append(neigbour)
        return max_color_val if visited_nodes == n else -1