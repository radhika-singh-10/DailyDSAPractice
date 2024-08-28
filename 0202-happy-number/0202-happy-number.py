class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            res=0
            while n:
                res+=(n%10)**2
                n//=10
            return res
        slow,fast=n,sumOfSquares(n)
            

        while slow!=fast:
            slow=sumOfSquares(slow)
            fast=sumOfSquares(sumOfSquares(fast))
        return True if slow==1 else False



                