class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ls,n=set(),len(nums)
        for i in range(n):
            if nums[i] in ls:
                return True
            ls.add(nums[i])
            if len(ls)>k:
                ls.remove(nums[i-k])

        return False


        # l,n=0,len(nums)
        # res=False
        # for r in range(l+1,n):
        #     while r<n-1 and nums[r]!=nums[l]:
        #         r=r+1
        #     if nums[r]==nums[l] and abs(r-l)<=k:
        #         print(nums[r],nums[l],r,l,nums[r]==nums[l],abs(nums[r]-nums[l]))
        #         return True
        #     l+=1

        # return False