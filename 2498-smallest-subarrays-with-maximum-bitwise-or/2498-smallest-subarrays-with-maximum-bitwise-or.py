class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # maxOr=0
        # for num in nums:
        #     maxOr|=num
        # memo=dict()
        #approach referred from editorial
        res,pos=[0]*(n),[0]*32
        for r in range(n-1,-1,-1):
            far=r
            for j in range(32):
                if (nums[r]>>j)&1:
                    pos[j]=r
                if pos[j]!=0:
                    far=max(far,pos[j])
            res[r]=far-r+1
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