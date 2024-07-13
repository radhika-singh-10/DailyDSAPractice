# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        # if not root:
        #     return 1
        def dfs(root,max_val):
            if not root:
                return 0
            if root.val>=max_val:
                res= 1
            else:
                res=0
            max_val=max(max_val,root.val)
            res+=dfs(root.left,max_val)
            res+=dfs(root.right,max_val)
            return res
        res=dfs(root,root.val)
        return res
