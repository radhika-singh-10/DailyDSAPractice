# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
       
        def dfs(node):
            if not node:
                return True, 0, float('inf'), float('-inf')
            left_bst,lhs,left_min_val,left_max_val=dfs(node.left)
            right_bst,rhs,right_min_val,right_max_val=dfs(node.right)

            if left_bst and right_bst and left_max_val < node.val < right_min_val:
                size = lhs + rhs + 1
                min_val,max_val = min(left_min_val, node.val),max(right_max_val, node.val)
                return True, size, min_val, max_val
            else:
                return False, max(lhs, rhs), 0, 0


        if not root:
            return 0
        _, res, _, _ = dfs(root)
        return res


        