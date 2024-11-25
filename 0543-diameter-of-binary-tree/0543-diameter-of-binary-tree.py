# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            res = 0
            def findHeight(root):
                if not root:
                    return 0
                else:
                    nonlocal res
                    lh = findHeight(root.left)
                    rh = findHeight(root.right)
                    res = max(res, lh + rh)
                    return 1 + max(lh, rh)

            findHeight(root)
            return res
