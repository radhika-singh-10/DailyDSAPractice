class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prefix,suffix=[1]*n,[1]*n
        for i in range(1,n):
            prefix[i]*=prefix[i-1]*nums[i-1]

        for i in reversed(range(n - 1)):
            suffix[i]*=suffix[i+1]*nums[i+1]

        for i in range(n):
            res[i]*=prefix[i]*suffix[i]

        return res
        # for i in range(1,n):
        #     res[i]=res[i-1]*nums[i-1]
        # p=1
        # for i in range(n-1,-1,-1):
        #     res[i]*=p
        #     p*=nums[i]

        # return res