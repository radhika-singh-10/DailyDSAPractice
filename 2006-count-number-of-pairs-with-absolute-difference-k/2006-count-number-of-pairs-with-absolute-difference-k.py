class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        #sliding window  concept - one ptr- fixed , other - moves
        #l->0-n-1
        #r->l+1->n
        res=0
        for l in range(len(nums)-1):
            r=l+1
            while r<len(nums):
                if abs(nums[r]-nums[l])==k:
                    res+=1
                r+=1

        return res
