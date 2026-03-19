class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res,cur_num,count=0,0,0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                res=max(res,count)
                count=0
                
        return max(count,res)
