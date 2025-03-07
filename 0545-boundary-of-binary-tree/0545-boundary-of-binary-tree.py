# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        #root - append in the res
        #iterative traverse left and check if the node has leaf which is not empty , append
        #traverse to leaf - dfs
        #iterative traverse right and check if the node has leaf which is not empty
        
        if not root:
            return []
        
        def isLeafNode(node):
            return not node.left and not node.right
        if root and isLeafNode(root):
            return [root.val]
        def getLeftBoundary(node):
            boundary=[]
            while node:
                if not isLeafNode(node):
                    boundary.append(node.val)
                if node.left:
                    node=node.left
                else:
                    node=node.right
                    
            return boundary
        
        def getRightBoundary(node):
            boundary=[]
            while node:
                if not isLeafNode(node):
                    boundary.append(node.val)
                if node.right:
                    node=node.right
                else:
                    node=node.left
                    
            return boundary[::-1]

        leaf=set()
        def getLeaves(node):
            if not node:
                return []
            if isLeafNode(node):
                #leaf.add(node.val)
                #return list(leaf)
                return [node.val]
            return getLeaves(node.left) + getLeaves(node.right)
            # return list(list(getLeaves(node.left)) + list(getLeaves(node.right)))
        
        left_boundary = getLeftBoundary(root.left) if root.left else []
        right_boundary = getRightBoundary(root.right) if root else []
        leaves = getLeaves(root) if root else []
        return [root.val] + left_boundary + leaves + right_boundary

            
            