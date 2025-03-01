# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #bfs-level by level traversal
        #store the sum of each node at each level and comapre it with res and replace it with res if res<cur_sum

        #0(h+n)-tc, sc-o(n)

        if not root:
            return 0

        queue=deque()
        res,level=1,0
        max_sum=root.val
        queue.append(root)

        while queue:
            level+=1
            cur_sum=0
            for _ in range(len(queue)):
                node=queue.popleft()
                cur_sum+=node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if cur_sum>max_sum:
                res=level
                max_sum=cur_sum
        return res


                