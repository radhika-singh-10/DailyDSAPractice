class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1,2,3] -> [1,3,2], [2,3,1]->[3,1,2], [3,2,1]->[1,2,3]
        #egde cases-> all elements equal?, unique/duplicate allowed?, list in decreasing order completely?-reverse
        #approach
        #if nums[i]<nums[i+1]:
        #else reverse 
        #for j in range(n-1,i,-1): if nums[j]>nums[i]
        #sc->o(1)
        
        n=len(nums)
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1

        if i>=0:
            j=n-1
            while nums[j]<=nums[i]:
                j-=1

            nums[i],nums[j]=nums[j],nums[i]
        
        nums[i+1:] = reversed(nums[i+1:])
        
