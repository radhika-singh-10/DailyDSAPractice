import random

class Solution:
    #w[i]/sum(w)
    def __init__(self, w: List[int]):
        self.cumulative_weights = []
        cumulative_sum = 0
        for weight in w:
            cumulative_sum += weight
            self.cumulative_weights.append(cumulative_sum)
        self.total_sum=cumulative_sum

    def pickIndex(self) -> int:
        target = self.total_sum*random.random()
        l,r=0,len(self.cumulative_weights)
        while l<r:
            m=l+(r-l)//2
            if self.cumulative_weights[m]<target:
                l=m+1
            elif self.cumulative_weights[m]>target:
                r=m
            else:
                return l
        return l
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()