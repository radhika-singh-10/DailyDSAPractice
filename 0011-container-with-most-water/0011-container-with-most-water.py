class Solution:
    def maxArea(self, height: List[int]) -> int:


        
        #edge cases->height==1->height[0]
        #any 0-> l=l+1
        #only positive number? no negative or 0 or decimal
        #what if - all the container height is same
        if len(height)==1:
            return height[0]
        res,l,r,max_area=0,0,len(height)-1,0
        while l<r:
            max_area=max(max_area,min(height[l],height[r])*abs(r-l))
            if height[l]<height[r]:
                l=l+1
            #elif height[r]>=height[l]:
            else:
                r=r-1
            # else:
            #     l+=1
            #     r-=1
            
        return max_area