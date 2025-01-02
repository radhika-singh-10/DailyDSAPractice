import math
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #max value of h - at least h papers having h index
        n=len(citations)
        if not citations:
            return 0
        elif n==1:
            if citations[0]>0:
                return n
            else:
                return 0
        h=math.ceil(n)
        l,r=0,n-1
        while l<=r:
            m=l+(r-l)//2
            if citations[m]==n-m:
                return citations[m]
            if citations[m]<n-m:
                l=m+1
            else:
                r=m-1
        return n-l