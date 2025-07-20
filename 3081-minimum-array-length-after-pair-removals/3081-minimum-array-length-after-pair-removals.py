class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        #binary search
        l,r=0,(len(nums)+1)//2
        res=len(nums)
        m=(r-l)//2
        while l<len(nums)//2 and r<len(nums):
            if nums[l]<nums[r]:
                res-=2
            l+=1
            r+=1
        return res


            

            

