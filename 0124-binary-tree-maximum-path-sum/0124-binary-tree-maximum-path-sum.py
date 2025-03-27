# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        res=-float("inf")
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            # if node.val>node.val+cur_sum:
            #     cur_sum=0
            # elif node.val+cur_sum>cur_sum:
            #     cur_sum+=node.val
            left_sum=max(0,dfs(node.left))
            right_sum=max(0,dfs(node.right))
            res=max(res,left_sum+right_sum+node.val)
            return max(left_sum+node.val,right_sum+node.val)
            #res=max(res,node.val+dfs(node.left,cur_sum)+dfs(node.right,cur_sum))
            #return res
            

        #res=max(res,dfs(root,0))
        dfs(root)
        return res