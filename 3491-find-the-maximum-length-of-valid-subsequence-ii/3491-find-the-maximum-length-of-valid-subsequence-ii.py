class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n,res=len(nums),0
        dp=[[0]*k for _ in range(k)]
        for num in nums:
            num%=k
            for prev in range(k):
                dp[prev][num]=dp[num][prev]+1
                res=max(res,dp[prev][num])
        return res