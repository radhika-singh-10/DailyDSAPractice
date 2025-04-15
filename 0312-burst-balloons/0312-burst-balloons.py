class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        res,n=0,len(nums)
        if n>1 and len(set(nums))==1:
            return (nums[0]**3)*(n-2)+nums[0]**2 +nums[0]
        nums=[1]+nums+[1]
        n+=2
        #question is similar to matrix multipliction 
        dp=[[0]*(n) for _ in range(n)]
        #get(i-1,nums)*nums[i]*get(i+1,nums)
        # for l in range(n-2,0,-1):
        #     for r in range(l,n-1):
        #         for i in range(l,r+1):
        #             gain=nums[l-1]*nums[i]*nums[r+1]
        #             remaining=dp[l][i-1]+dp[i+1][r]
        #             dp[l][r]=max(remaining+gain,dp[l][r])
        # return dp[1][n-2]
        for k in range(2,n):
            for l in range(n-k):
                r=l+k
                for i in range(l+1,r):
                    dp[l][r]=max(dp[l][r],nums[l]*nums[i]*nums[r]+dp[l][i]+dp[i][r])
        return dp[0][n-1]



        


        

