# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        #dfs - recursively calculate the zig_zag_path and compare with the res (min val) replace
        #zig zag logic
        #false-left,true-right -> when need to go left, else opposite
        #
        self.res=0
        if not root:
            return 0
        def dfs(node,turn,path):
            if not node:
                return 
            self.res=max(self.res,path)
            if turn:
                dfs(node.left,False,path+1)
                dfs(node.right,True,1)
            else:
                dfs(node.right,True,path+1)
                dfs(node.left,False,1)

        
        dfs(root,True,0)
        return self.res

        