class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums=nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res=0
        for i,j in zip(self.nums,vec.nums):
            res+=i*j
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)