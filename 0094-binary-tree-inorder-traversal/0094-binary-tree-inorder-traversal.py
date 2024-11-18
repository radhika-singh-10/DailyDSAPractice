# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #appraoch - check if node is present-> if not ->return list
        #inorder->left,root,right
        #left-dfs(root.left,res) , untill left is null,res.append(root.val)
        #res.append(root.val)
        #traverse right dfs(root.right,res), untill right is null, res.append(root.right.val)
        #[1,null,2,3] -> [1,3,2]
        #preorder [2,1,null,null,3,4,null] -> [1,2,4,3]
        res=[]
        def dfs(root,res):
            if not root:
                return 
            dfs(root.left,res)
            res.append(root.val)
            dfs(root.right,res)

        dfs(root,res)
        return res




