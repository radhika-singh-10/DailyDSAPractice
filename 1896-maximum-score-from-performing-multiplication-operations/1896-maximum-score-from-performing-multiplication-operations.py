class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n,m=len(nums),len(multipliers)
        #followed hint1,2,3
        dp=[[0]*(m+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for l in range(i,-1,-1):
                mul=multipliers[i]
                r=n-1-(i-l)
                dp[i][l]=max(mul*nums[l]+dp[i+1][l+1],mul*nums[r]+dp[i+1][l])
        return dp[0][0]
