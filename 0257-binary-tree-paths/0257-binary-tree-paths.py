# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        def traverse(root,p):
            if not root:
                return res
            if not root.left and not root.right:
                p.append(str(root.val))
                res.append("->".join(p))
                p.pop()

            p.append(str(root.val))
            traverse(root.left,p)
            traverse(root.right,p)
            p.pop()

        traverse(root,[])
        return res

                
        