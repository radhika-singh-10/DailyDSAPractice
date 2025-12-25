class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        non_incr_left,non_decr_right=[1]*n,[1]*n
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                non_incr_left[i]=non_incr_left[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]<=nums[i+1]:
                non_decr_right[i]=non_decr_right[i+1]+1
        for i in range(k,n-k):
            if non_incr_left[i-1]>=k and non_decr_right[i+1]>=k:
                res.append(i)
        return res