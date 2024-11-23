# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        #edge case 1-> root is empty -> return []
        #dfs->recursive
        #while root:dfs(root)
        #condition - if not root.left and not root.right -> res[-1].append(root.val)
        res=[]
        def dfs(node):
            if not node:
                return None #break recursion 
            if not node.left and not node.right:
                res[-1].append(node.val)
                return None
            
            node.left=dfs(node.left)
            node.right=dfs(node.right)
            return node
        
        while root:
            res.append([])
            root=dfs(root)
        return res

