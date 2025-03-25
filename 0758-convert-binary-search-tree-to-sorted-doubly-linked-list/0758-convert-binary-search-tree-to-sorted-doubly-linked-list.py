"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #meta interview question - 21st november 2024 - reject
        #modification - bt - logic same
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            nonlocal first,last
            if last:
                last.right=node
                node.left=last
            else:
                first=node
            last=node
            dfs(node.right)

        if not root:
            return
        first,last=None,None
        dfs(root)
        last.right=first
        first.left=last
        return first

        

