"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        queue, visited = deque([node]), {node.val: Node(node.val, [])}
        while queue:
            cur=queue.popleft()
            cur_clone = visited[cur.val]
            for n in cur.neighbors:
                if n.val not in visited:
                    visited[n.val]=Node(n.val,[])
                    queue.append(n)
                    
                cur_clone.neighbors.append(visited[n.val])

        return visited[node.val]

        
