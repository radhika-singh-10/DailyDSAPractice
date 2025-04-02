class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        res=1
        max_step=nums[0]
        e=nums[0]
        for i in range(1,len(nums)-1):
            max_step=max(max_step,i+nums[i])
            if i==e:
                e=max_step
                res+=1
        return res