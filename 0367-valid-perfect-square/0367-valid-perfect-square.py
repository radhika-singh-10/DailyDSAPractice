class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        l,r=1,num//2
        while l<=r:
            m=l+(r-l)//2
            temp=m*m
            if temp==num:
                return True
            elif temp>num:
                r=m-1
            else:
                l=m+1
        return False
            

