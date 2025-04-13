class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res,seen,dup=set(),{},set()
        for i, val1 in enumerate(nums):
            if val1 not in dup:
                dup.add(val1)
                for j,val2 in enumerate(nums[i+1:]):
                    complement=-val1-val2
                    if complement in seen and seen[complement]==i:
                        res.add(tuple(sorted((val1,val2,complement))))
                    seen[val2]=i
        return [list(x) for x in res]
        # res=[]
        # nums.sort()
        # for i in range(0,len(nums)):
        #     #to handle duplicacy
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     j,k=i+1,len(nums)-1
        #     while j<k:
        #         total=nums[i]+nums[j]+nums[k]
        #         if total==0:
        #             res.append([nums[i],nums[j],nums[k]])
        #             while j < k and nums[j] == nums[j + 1]:
        #                 j+=1
        #             while k>j and nums[k]==nums[k-1]:
        #                 k-=1
        #             j+=1
        #             k-=1 
        #         elif total<0:
        #             j+=1
        #         else:
        #             k-=1
        # return res