class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #approach
        #kadane's algorithm 

        #l,r-2ptr approach
        #while r<len(nums) and cur_sum +nums[r]>=cur_sum: r=r+1
        #if cur_sum+nums[r]<cur_sum: r=r+1, l=r
        #res=max(res,cur_sum)
        #tc-0(n), sc-0(1)

        n,l,res,cur_sum=len(nums),0,-float('inf'),0
        for r in range(n):
            cur_sum+=nums[r]
            res=max(res,cur_sum)
            while r<n and cur_sum<0:
                cur_sum-=nums[l]
                l+=1
            

        return res
            
