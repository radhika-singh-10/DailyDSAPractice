class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res,n=0,len(nums)
        prefix=[0]*(n+1)
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+nums[i-1]
        for i in range(n):
            start=max(0,i-nums[i])
            res+=prefix[i+1]-prefix[start]

        return res
