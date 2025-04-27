class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        prefix_sum,freq,res,n=0,{0:1},0,len(nums)
        for i in range(n):
            prefix_sum+=nums[i]
            if prefix_sum-k in freq:
                res+=freq[prefix_sum-k]
            if prefix_sum in freq:
                freq[prefix_sum] += 1
            else:
                freq[prefix_sum] = 1
        return res


        # prefix_sum,n,res,l=0,len(nums),0,0
        # for r in range(n):
        #     if prefix_sum+nums[r]<=k:
        #         prefix_sum+=nums[r]

        #     if prefix_sum==k:
        #         res+=1
        #         prefix_sum-=nums[l]
        #         l=l+1
            
        # return res