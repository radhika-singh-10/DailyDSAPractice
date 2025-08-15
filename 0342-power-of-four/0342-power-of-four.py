class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n==1 or n!=0==n%4 and self.isPowerOfFour(n//4)