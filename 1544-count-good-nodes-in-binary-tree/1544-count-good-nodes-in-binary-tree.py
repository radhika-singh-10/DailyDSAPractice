# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(node,max_val):
            if not node:
                return 0
            max_val=max(node.val,max_val)
            if node.val>=max_val:
                return 1+dfs(node.left,max_val)+dfs(node.right,max_val)
            else:
                return dfs(node.left,max_val)+dfs(node.right,max_val)
            
        res=dfs(root,root.val)
        return res
