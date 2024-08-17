class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        res=0
        sorted_nums = sorted(nums)
        l, r = len(nums) - 1,0
        for i in range(n):
            if nums[i]!=sorted_nums[i]:
                l,r=min(l,i),max(r,i)

        return 0 if l>=r else abs(r-l+1)


        

        