from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited,queue=set(),deque()
        res=0
        graph = defaultdict(list)
        
        for a, b in connections:
            graph[a].append((b, 1)) 
            graph[b].append((a, 0))

        visited.add(0)
        queue = deque([0])
        while queue:
            cur=queue.popleft()
            for i,count in graph[cur]:
                if i not in visited:
                    visited.add(i)
                    res+=count
                    queue.append(i)

        return res