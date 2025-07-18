class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp
        n=len(nums)
        dp=[1]*(n)
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                
        return dp[-1]

        # dp=[0]*(n+1)
        # if n==1:
        #     return 1
        # elif n==2:
        #     if nums[0]<nums[1]:
        #         return 2
        #     else:
        #         return 1
        # else:
        #     dp=[nums[0]]
        #     for i in range(n):
        #         num=nums[i]
        #         if num>dp[-1]:
        #             dp.append(num)
        #         else:
        #             index=bisect_left(dp, num)
        #             if index==len(dp):
        #                 dp.append(num)
        #             else:
        #                 dp[index]=num
        #     return len(dp)



        