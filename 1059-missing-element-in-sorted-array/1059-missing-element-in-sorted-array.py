class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        #sorted -> binary search
        n = len(nums)
        def missing(i: int) -> int:
            return nums[i] - nums[0] - i
        if k > missing(n - 1):
            return nums[-1] + (k - missing(n - 1))

        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if missing(m) < k:
                l = m + 1
            else:
                r = m
        p = l - 1
        return nums[p] + (k - missing(p))

        
        # l,r,res=0,len(nums)-1,0
        # while l<=r:
        #     m=l+(r-l)//2
        #     countMissingElement=nums[m]-nums[l]-(m-l)
        #     if countMissingElement>=k:
        #         r=m
        #     else:
        #         k-=countMissingElement
        #         l=m+1

        # return nums[0]+l
                
            


            




