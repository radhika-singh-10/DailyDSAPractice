# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #perform inroder traversal
        #insert in array
        #take mid as root -> construct tree recrusively
        if not root:
            return
        nodeList=[] 
        self.performInorderTraversal(root,nodeList)
        return self.createBalancedBst(nodeList,0,len(nodeList)-1)
        
    def performInorderTraversal(self,node,nodeList):
        if not node:
            return 
        self.performInorderTraversal(node.left,nodeList)
        nodeList.append(node.val)
        self.performInorderTraversal(node.right,nodeList)
    def createBalancedBst(self,nodeList,left,right):
        #print(left,right,nodeList)
        if left>right:
            return None
        #print(left,right,nodeList)
        mid=left+(right-left)//2
        left_subtree=self.createBalancedBst(nodeList,left,mid-1)
        right_subtree=self.createBalancedBst(nodeList,mid+1,right)
        node=TreeNode(nodeList[mid],left_subtree,right_subtree)
        return node

        

            
            
        