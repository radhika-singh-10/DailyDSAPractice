class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        maxArea=0
        l,r=0,n-1
        while l<r:
            maxArea=max(maxArea,(r-l)*min(height[r],height[l]))
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return maxArea
