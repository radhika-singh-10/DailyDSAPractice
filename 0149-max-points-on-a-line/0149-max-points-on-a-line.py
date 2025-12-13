class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        
        res=1
        def getSlopes(p1,p2):
            x1,y1=p1
            x2,y2=p2
            if x1-x2==0:
                return float('inf')
            return (y1-y2)/(x1-x2)

        for i,p1 in enumerate(points):
            slopes=defaultdict(int)
            for j,p2 in enumerate(points[i+1:]):
                slope=getSlopes(p1,p2)
                slopes[slope]+=1
                res=max(res,slopes[slope])
        return res+1
