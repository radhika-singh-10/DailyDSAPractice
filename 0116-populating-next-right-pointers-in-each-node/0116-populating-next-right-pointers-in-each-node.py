"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        visited,queue=set(),deque([root]) 
        while queue:
            right_node=None
            for i in range(len(queue)):
                cur_node=queue.popleft()
                cur_node.next,right_node=right_node,cur_node
                if cur_node.right:
                    queue.extend([cur_node.right,cur_node.left])
        return root

        