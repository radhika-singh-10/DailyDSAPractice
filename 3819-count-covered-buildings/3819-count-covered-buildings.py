from collections import defaultdict
from bisect import bisect_left
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        horizontal,vertical,res=defaultdict(list),defaultdict(list),0
        for x,y in buildings:
            horizontal[y].append(x)
            vertical[x].append(y)
        #print(horizontal,vertical)
        for y in horizontal:
            horizontal[y].sort()
        for x in vertical:
            vertical[x].sort()
        #print(horizontal,vertical)
        for x,y in buildings:
            xs,ys=horizontal[y],vertical[x]
            i,j=bisect_left(xs,x),bisect_left(ys,y)
            if (i>0) and (i<len(xs)-1) and (j>0) and (j<len(ys)-1):
                res+=1
        return res
        # ans = 0
        # rows,cols = defaultdict(list),defaultdict(list)

        # for x, y in buildings:
        #     rows[y].append(x)
        #     cols[x].append(y)
        # for y in rows:
        #     rows[y].sort()
        # for x in cols:
        #     cols[x].sort()

        # for x, y in buildings:
        #     xs = rows[y]
        #     ys = cols[x]
        #     i = bisect.bisect_left(xs, x)
        #     j = bisect.bisect_left(ys, y)
        #     has_left = (i > 0)
        #     has_right = (i < len(xs) - 1)
        #     has_above = (j > 0)
        #     has_below = (j < len(ys) - 1)

        #     if has_left and has_right and has_above and has_below:
        #         ans += 1

        # return ans