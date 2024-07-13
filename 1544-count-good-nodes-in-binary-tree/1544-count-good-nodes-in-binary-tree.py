# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(root,max_val):
            if not root:
                return 0
            max_val=max(root.val,max_val)
            if root.val>=max_val:
                return 1+dfs(root.left,max_val)+dfs(root.right,max_val)
            else:
                return dfs(root.left,max_val)+dfs(root.right,max_val)
            
        res=dfs(root,root.val)
        return res
