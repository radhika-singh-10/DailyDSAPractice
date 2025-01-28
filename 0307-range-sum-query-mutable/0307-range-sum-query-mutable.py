from typing import List

class SegmentTree:
    def __init__(self, total, l, r):
        self.sum = total
        self.left = None
        self.right = None
        self.l = l
        self.r = r

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, l, r):
        if l == r:
            # Leaf node
            return SegmentTree(nums[l], l, r)
        
        m = (l + r) // 2
        root = SegmentTree(0, l, r)
        root.left = self.build(nums, l, m)
        root.right = self.build(nums, m + 1, r)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        def updateTree(node, index, val):
            if node.l == node.r:  # Leaf node
                node.sum = val
                return
            
            m = (node.l + node.r) // 2
            if index <= m:
                updateTree(node.left, index, val)
            else:
                updateTree(node.right, index, val)
            
            # Update the sum of the current node
            node.sum = node.left.sum + node.right.sum

        updateTree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def rangeSum(node, left, right):
            if node.l == left and node.r == right:
                return node.sum
            
            m = (node.l + node.r) // 2
            if right <= m:
                return rangeSum(node.left, left, right)
            elif left > m:
                return rangeSum(node.right, left, right)
            else:
                return rangeSum(node.left, left, m) + rangeSum(node.right, m + 1, right)

        return rangeSum(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)