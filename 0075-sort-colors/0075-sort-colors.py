class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=o=t=0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            elif nums[i]==1:
                o+=1
            else:
                t+=1
        for i in range(len(nums)):
            if z>0:
                nums[i]=0
                z-=1
            elif o>0:
                nums[i]=1
                o-=1
            else:
                nums[i]=2
                t-=1
        
        