# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeList = defaultdict(list)
        queue = deque([(root,0,0)]) 
        while queue:
            for i in range(len(queue)):
                node,row,col = queue.popleft()
                nodeList[col].append((row,node.val))
                if node.left:
                    queue.append((node.left,row+1,col-1))
                if node.right:
                    queue.append((node.right,row+1,col+1))
        result = []
        for col in sorted(nodeList.keys()):
            nodes = sorted(nodeList[col])
            result.append([val for i,val in nodes])
        return result