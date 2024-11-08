# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root):
            if not root:
                return 0
            res=0
            if root and root.val>=low and root.val<=high:
                res+=root.val
            lhs=dfs(root.left)
            rhs=dfs(root.right)
            return lhs+rhs+res
        return dfs(root)

            
