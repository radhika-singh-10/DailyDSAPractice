class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        size=2*k+1
        return ceil(n/size)*ceil(m/size)
