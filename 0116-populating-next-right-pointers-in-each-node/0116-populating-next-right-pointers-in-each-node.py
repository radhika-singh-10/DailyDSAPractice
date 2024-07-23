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

        #incorrect logic
        # level, res, d = 0, [], {}
        
        # def find_level(node, level):
        #     if not node:
        #         return d
        #     if level not in d:
        #         d[level] = []
        #     d[level].append(node.val)
        #     find_level(node.left, level + 1)
        #     find_level(node.right, level + 1)

        # find_level(root, level)
        
        # for key in d:
            
        #     for v in d[key]:
        #         print(d[key],v)
        #         res.append(v)
        #     res.append('#')

        