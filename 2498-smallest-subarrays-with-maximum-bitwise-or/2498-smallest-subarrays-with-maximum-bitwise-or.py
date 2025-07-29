class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # maxOr=0
        # for num in nums:
        #     maxOr|=num
        # memo=dict()
        res,pos=[0]*(n),[-1]*32
        for l in range(n-1,-1,-1):
            far=l
            for j in range(32):
                if (nums[l]>>j) & 1:
                    pos[j]=l
                if pos[j]!=-1:
                    far=max(far,pos[j])
            res[l]=far-l+1
        return res
        # def backtrack(idx,curOr,l,r):
            
        #     if curOr==maxOr:
        #         res[r-l+1]=idx
        #         return 
        #     if idx==n:
        #         return
            
            
        #     #backtrack(idx+1,curOr,l+1,r)
        #     backtrack(idx+1,curOr|nums[idx],l+1,r)





        # backtrack(0,0,0,n-1)
        # return res