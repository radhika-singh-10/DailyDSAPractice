# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        #two var, a,b-> initially max
        #a-min val
        #b-2nd min val
        #a<b and b<=node.val 
        #after full iteration a==b -> -1
        if not root:
            return -1
        a,b=float("inf"),root.val
        def dfs(node):
            nonlocal a,b
            if not node:
                return 
            
            if a > node.val:
                b, a = a, node.val
            elif a < node.val < b:
                b = node.val  
            
            
            dfs(node.left)
            dfs(node.right)
            
            

        dfs(root)
        return b if b < float("inf") else -1