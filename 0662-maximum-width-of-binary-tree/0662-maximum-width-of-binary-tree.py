# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxWidth=0
        queue=deque()
        queue.append((root,0))
        while queue:
            levelLength=len(queue)
            _,levelHeadIndex=queue[0]
            for _ in range(levelLength):
                node,colIndex=queue.popleft()
                if node.left:
                    queue.append((node.left,2*colIndex))
                if node.right:
                    queue.append((node.right,2*colIndex+1))
            maxWidth=max(maxWidth,colIndex-levelHeadIndex+1)
        return maxWidth
            
