class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp
        n=len(nums)
        dp=[0]*(n+1)
        if n==1:
            return 1
        elif n==2:
            if nums[0]<nums[1]:
                return 2
            else:
                return 1
        else:
            dp=[nums[0]]
            for i in range(n):
                num=nums[i]
                if num>dp[-1]:
                    dp.append(num)
                else:
                    index=bisect_left(dp, num)
                    if index==len(dp):
                        dp.append(num)
                    else:
                        dp[index]=num
            return len(dp)



        