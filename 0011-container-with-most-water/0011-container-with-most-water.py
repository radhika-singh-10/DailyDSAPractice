class Solution:
    def maxArea(self, height: List[int]) -> int:
        #edge cases->height==1->height[0]
        #any 0-> l=l+1
        #only positive number? no negative or 0 or decimal

        if len(height)==1:
            return height[0]
        res,l,r,max_area=0,0,len(height)-1,0
        while l<r:
            max_area=max(max_area,min(height[l],height[r])*abs(r-l))
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
            
        return max_area