class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        maxArea=0
        l,r=0,n-1
        #min(height[l],height[i]) * (i-l-1)
        while l<r:
            maxArea=max(maxArea,min(height[r],height[l])*(r-l))
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
        return maxArea
            
