class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n,m=len(nums),len(multipliers)
        #followed hint1,2,3
        #Greedy is short-sighted. For the global optimum, we pick the local optimum. But picking this Local Optimum may restrict greater positive product afterward. Moreover, what if both ends of nums are identical? We don't know which one to favor. One may yield another score, another may yield a very different score.
        dp=[[0]*(m+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for l in range(i,-1,-1):
                mul=multipliers[i]
                r=n-1-(i-l)
                #print(r,l,dp,mul,nums[l],nums[r])
                dp[i][l]=max(mul*nums[l]+dp[i+1][l+1],mul*nums[r]+dp[i+1][l])
        return dp[0][0]
