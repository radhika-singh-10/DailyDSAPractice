import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search - sorted
        #edge cases-> no element->0, int?, fract?, negative, 0, positive, unqiue/duplicate??
        #set a formula for it
        #we check for rotation -> where it is present in the list
        #if nums[m]>nums[r]: l=m-1
        #elif nums[m]<nums[r]: r=m+1
        #else: r-=1 (check linearly)
        
        #tc-0(nlogn) sc->0(1)
        #[5,5,6,7,1,3,4,5]
        n=len(nums)
        if not nums:
            return 0
        elif n==1:
            return nums[0]
        else:
            count=0
            res=sys.maxsize
            l,r=0,len(nums)-1
            while l<=r:
                m=l+(r-l)//2
                if nums[m]>nums[r]:
                    l=m+1
                elif nums[m]<nums[r]:
                    r=m
                else:
                    r-=1
                
                    
        return nums[l]      

