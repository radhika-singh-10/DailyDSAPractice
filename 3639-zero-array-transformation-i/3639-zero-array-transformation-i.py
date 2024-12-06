class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        res=False
        #edge cases
        #if not queries->check if zero in nums->return true else false
        #if not nums->return false
        #only +ive int-> negative??,zeroes??[sparsh matrix], fraction 
        #approach
        #check index l,r=queries[i][0],queries[i][1]->if in range of nums->check if nums[j]>0>nums[j]-=1
        #tc->o(n*m),sc->o(1)
        # if not nums:
        #     return False
        # if not queries: 
        #     return all(x == 0 for x in nums)
        # for query in queries:
        #     l, r = query
        #     if 0 <= l <= r < len(nums):
        #         for i in range(l, r + 1):
        #             if nums[i] > 0:
        #                 nums[i] -= 1

        # return all(x == 0 for x in nums)
        diff = [0] * (len(nums) + 1)
        for l,r in queries:
            diff[l]+=1
            diff[r+1]-=1
        cur=0
        for e,d in zip(nums,diff):
            cur+=d
            if e-cur>0:
                return False

        return True
            
