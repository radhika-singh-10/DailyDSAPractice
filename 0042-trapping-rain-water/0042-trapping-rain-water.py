class Solution:
    def trap(self, height: List[int]) -> int:
        left,right,max_right,max_left,res=0,len(height)-1,0,0,0
        #min of (left,right) * (right-left+1)
        while left<right:
            #print(left,right,res,max_left,max_right)
            if height[left]<height[right]:
                max_left=max(max_left,height[left])
                res+=max_left-height[left]
                left+=1
            else:
                max_right=max(max_right,height[right])
                res+=max_right-height[right]
                right-=1

        return res
            