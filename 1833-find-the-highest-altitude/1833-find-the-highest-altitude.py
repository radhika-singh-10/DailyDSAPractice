class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0]
        for i in range(0,len(gain)):
            res.append(gain[i]+res[-1])
        return max(res)
