# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res,queue=[],deque([root])
        if not root:
            return res
        
        while queue:
            right_node=None
            for i in range(len(queue)):
                cur=queue.popleft()
                if cur:
                    right_node=cur
                    queue.append(cur.left)
                    queue.append(cur.right)
            if right_node:
                res.append(right_node.val)
        return res
