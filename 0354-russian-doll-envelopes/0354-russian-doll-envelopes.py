import heapq
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #we sort accoridng to width and height (increasing)
        #pattern- dp lis for both width and height
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        res,n=0,len(envelopes)
        def lis(nums):
            dp=[]
            for i in range(len(nums)):
                index=bisect_left(dp,nums[i])
                if index==len(dp):
                    dp.append(nums[i])
                else:
                    dp[index]=nums[i]
            return len(dp)
        return lis([i[1] for i in envelopes])
        

        return lis


