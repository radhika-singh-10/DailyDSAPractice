class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos,res=0,False
        for i in range(len(nums)):
            if pos<i:
                return False
            pos=max(pos,i+nums[i])

        return True