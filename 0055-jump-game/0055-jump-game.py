class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos,n=0,len(nums)
        for i in range(n):
            if pos<i:
                return False
            pos=max(pos,i+nums[i])

        return True










        # pos,res=0,False
        # for i in range(len(nums)):
        #     if pos<i:
        #         return False
        #     pos=max(pos,i+nums[i])

        # return True