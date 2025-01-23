# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        def findMin(root):
            cur=root
            while cur and cur.left:
                cur=cur.left
            return cur
        def remove(root,key):
            if not root:
                return None
            if root.val<key:
                root.right=remove(root.right,key)
            elif root.val>key:
                root.left=remove(root.left,key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min_node=findMin(root.right)
                    root.val=min_node.val
                    root.right=remove(root.right,min_node.val)
            return root
        return remove(root,key)
