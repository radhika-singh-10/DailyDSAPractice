import random
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000 :
            return 1.0
        m=ceil(n/25)
        #servings={(100,0),(75,25),(25,75),(0,100)}
        dp = defaultdict(dict)
        def calculateDp(i,j):
            if i<=0 and j<=0:
                return 0.5
            if i<=0:
                return 1.0
            if j<=0:
                return 0.0
            if i in dp and j in dp[i]:
                return dp[i][j]
            dp[i][j]=(calculateDp(i-4,j)+calculateDp(i-3,j-1)+calculateDp(i-2,j-2)+calculateDp(i-1,j-3))/4.0
            return dp[i][j]

        for i in range(1, m + 1):
            if calculateDp(i, i) > 1 - 1e-5:
                return 1.0
        return calculateDp(m, m)