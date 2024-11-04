# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        column_table = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            
            node, column=queue.popleft()
            if node:
                column_table[column].append(node.val)
                queue.append((node.left,column-1))
                queue.append((node.right,column+1))


        sorted_columns=sorted(column_table.items())

        return [val for _,val in sorted_columns]



                
        


                


            
