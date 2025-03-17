class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res,n=0,len(nums)
        if n < 3:
            return 0
        for i in range(2,n):
            l,r=0,i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    res+=(r-l)   
                    r-=1
                else:
                    l+=1         
        return res

        # for i in range(len(nums)-2):
        #     j,k=i+1,len(nums)-1
        #     while j<k:
        #         if nums[k]+nums[i]>nums[j]:
        #             res+=k-j
        #             k-=1
        #         else:
        #             j+=1
        # return res