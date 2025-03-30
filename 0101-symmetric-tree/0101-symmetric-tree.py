# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            # print(p,q)
            # if p:
            #     print(p.val)
            # if q:
            #     print(q.val)
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            
            # if p and p.left and p.right and q and q.left and q.right and p.val==q.val:
            return dfs(p.left,q.right) and dfs(p.right,q.left) 
            
        if not root:
            return False
        return dfs(root.left,root.right)
        
                