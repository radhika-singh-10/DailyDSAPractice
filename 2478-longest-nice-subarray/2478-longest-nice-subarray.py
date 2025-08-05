class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n,l,res,used=len(nums),0,0,0
        for r in range(len(nums)):
            while used & nums[r]!=0:
                used^=nums[l]
                l+=1
            used|=nums[r]
            res=max(res,r-l+1)
        return res
            
                

            


