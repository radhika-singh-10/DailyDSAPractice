class Solution:
    def trap(self, height: List[int]) -> int:
        #edge case->empty height arr,no negative, only int, only 0 -> 0
        if not height:
            return 0
        #two pointer
        l,r=0,len(height)-1
        max_right,max_left,max_area=height[r],height[l],0
        #l->non-zero,max_height=0
        #when it beocmes non zero, ->r=r-1 max_height=max(max_height,r)=> max_area=max(max_area,min(height[l],height[r])*abs(r-l))
        #
        #if l<max_left=>check for max_area=>if less, l=l+1
        #else max_left=l
        #same for right
        #
        while l<r:
                if max_left<max_right:
                    max_area+=max_left-height[l]
                    l+=1
                    max_left=max(max_left,height[l])
                else:
                    max_area+=max_right-height[r]
                    r-=1
                    max_right=max(max_right,height[r])
        return max_area




