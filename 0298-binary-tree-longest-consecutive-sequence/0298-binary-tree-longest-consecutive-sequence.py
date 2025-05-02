# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res=1
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            lh,rh = dfs(node.left),dfs(node.right)
            lh = 1+lh if (node.left and node.left.val==node.val+1) else 1
            rh= 1+rh if (node.right and node.right.val==node.val+1) else 1
            # if node.left and node.val+1==node.left.val:
            #     lh=max(lh,1+dfs(node.left))
            # if node.right and node.val+1==node.right.val:
            #     rh=max(rh,1+dfs(node.right))
            res=max(res,lh,rh)
            return max(lh,rh)

        dfs(root)   
        return res

            
                
            
        