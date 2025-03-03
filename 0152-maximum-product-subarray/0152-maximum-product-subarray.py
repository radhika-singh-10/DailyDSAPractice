class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        max_prod = nums[0]  
        cur_max, cur_min = nums[0], nums[0]  
        for i in range(1, len(nums)):
            if nums[i] < 0:  
                cur_max, cur_min = cur_min, cur_max  
            cur_max = max(nums[i], cur_max * nums[i])  
            cur_min = min(nums[i], cur_min * nums[i]) 

            max_prod = max(max_prod, cur_max)  
        return max_prod
        # max_prod,cur_prod=-float("inf"),1
        # #2 ptr apporach - l,rn=0,len(nums)
        # #max_prod=max(max_prod,cur_prod)
        # #cur_prod*=nums[r]
        # #if cur_prod<0: cur_prod=int(cur_prod/nums[l]) l=l+1
        # l=nums[0]
        # for r in range(n):
            
        #     max_prod=max(max_prod,cur_prod)
        #     if cur_prod*nums[r]<cur_prod: 
        #         cur_prod=0
        #     else:
        #         cur_prod*=nums[r]
            

        # return max_prod
                






        # # if len(nums)==1:
        # #     return nums[0]
        # # else:
        # #     res=[]
        # #     nums.sort()
        # #     m=1
        # #     i=0
        # #     for i in nums:
        # #         t=max(m,m*i)
        # #         t*=m
        # #     return t
        # # if len(nums)==1:
        # #     return nums[0]
        # # max_prod,l=0,0
        # # for l in range(len(nums)):
        # #     r=l+1
        # #     prod=nums[l]
        # #     while r<len(nums):
        # #         prod*=nums[r]
        # #         max_prod=max(max_prod,prod)
        # #         r+=1
        
        # # # for i in range(len(nums)-1):
        # # #     max_prod=max(max_prod,nums[i]*nums[i+1])
        # # return max_prod
        