class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums={}
        for i,n in enumerate(nums):
            if nums[i]!=0:
                self.nums[i]=n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res=0
        for i,j in self.nums.items():
            if i in vec.nums:
                res+=vec.nums[i]*j
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)