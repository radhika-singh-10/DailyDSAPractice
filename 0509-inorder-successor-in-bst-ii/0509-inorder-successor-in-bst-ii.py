"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        #preorder is given- need to generate inorder and then find the succesor
        if not node:
            return None
        elif node.right:
            node=node.right
            while node and node.left:
                node=node.left
            return node
        while node.parent and node==node.parent.right:
            node=node.parent
        return node.parent
