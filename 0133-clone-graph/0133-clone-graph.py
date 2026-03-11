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
        queue, clone = deque([node]), {node.val: Node(node.val, [])}
        while queue:
            cur=queue.popleft()
            cur_clone = clone[cur.val]
            for n in cur.neighbors:
                if n.val not in clone:
                    clone[n.val]=Node(n.val,[])
                    queue.append(n)
                    
                cur_clone.neighbors.append(clone[n.val])

        return clone[node.val]

        
