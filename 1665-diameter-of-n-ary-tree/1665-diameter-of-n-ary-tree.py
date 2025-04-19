"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    #mock interview question
    #intuition - we need to select the top 2 max height from the tree
    #either it is root-leaf, leaf-leaf 
    #we can store the heights in a set, and get top 2 heights - easier but more space and may exceed space complexity
    #we can compare the cur_height with max_height2-> we apply three numbers swap logic - if greater than both, then max_height_two=max_height_one, max_height_one=cur_height, elif grater than max_height_two -> max_height_two=cur_height

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        res=0
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            if len(node.children)==0:
                return 0
            max_height_one,max_height_two=0,0
            for child in node.children:
                cur_height=1+dfs(child)
                if cur_height>max_height_one:
                    max_height_two,max_height_one=max_height_one,cur_height
                elif cur_height>max_height_two:
                    max_height_two=cur_height
            distance=max_height_two+max_height_one
            res=max(res,distance)
            return max_height_one
        dfs(root)
        return res
