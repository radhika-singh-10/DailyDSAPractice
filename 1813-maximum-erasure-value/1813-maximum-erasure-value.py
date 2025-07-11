class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        l,res,uniqueSet,currentSum=0,0,set(),0
        #check for uniqueness in the subarray
        #check with res for max sum
        for r in range(n):
            
            while nums[r] in uniqueSet:
                uniqueSet.remove(nums[l])
                currentSum-=nums[l]
                l+=1
            
            uniqueSet.add(nums[r])
            currentSum += nums[r]
            r+=1
            res=max(res,currentSum)
        return res

        



