class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res=big=0
        nums.sort(key = lambda x:x[0])
        heap=[nums[0]]
        for a,b in nums:
            res+=max(0,b-max(a-1,big))
            big=max(big,b)
        return res
