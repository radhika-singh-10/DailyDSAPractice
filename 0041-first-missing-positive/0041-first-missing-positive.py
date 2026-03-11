class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        #cycle sort
        i=0
        while i<n:
            correctIdx=nums[i]-1
            if 0<nums[i]<=n and nums[i]!=nums[correctIdx]:
                nums[i],nums[correctIdx]=nums[correctIdx],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
        # seen=[False]*(n+1)
        # for num in nums:
        #     if 0 < num <= n:
        #         seen[num]=True
        # for i in range(1,n+1):
        #     if not seen[i]:
        #         return i
        # return n+1
        # s=[1:n+1]
        # sumRange=sum(s)
        # checkSum=sum(i for i in nums)
        # return sumRange-checkSum