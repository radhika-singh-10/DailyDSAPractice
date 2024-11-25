# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        #calculate the height -> r,c(dfs)
        #traverse in-order and store the sequence(dfs)
        #[1,2]->inorder->[2,1,null] , [1,2,3,null,4]->[null,2,4,1,null,3]
        #observation - the root is in the middle and the top of the matrix(1st row, middle column)
        #the left subtree would be in the next rows and the first half of the columns
        #the right subtree would be in the same rows but the second half of the column
        #offset->offset//2
        #col->col-offset[left], col->col+offset[right]
        #place accoridng the inorder in the matrix
        def calculateHeight(root):
            if not root:
                return 0
            return max(1+calculateHeight(root.left),1+calculateHeight(root.right))
        

        if not root:
            return [[]]
        height=calculateHeight(root)
        res=[[""]*(2**(height)-1) for _ in range(height)]
        col=2**(height)-1
        row=height
        def inorderAssignment(node,row,col,offset):
            if not node:
                return 
            #left, root, right->inorder
            res[row][col]=str(node.val)
            inorderAssignment(node.left,row+1,col-offset,offset//2)
            inorderAssignment(node.right,row+1,col+offset,offset//2)
        inorderAssignment(root,0,(col-1)//2,2**(height-2))
        return res
        
