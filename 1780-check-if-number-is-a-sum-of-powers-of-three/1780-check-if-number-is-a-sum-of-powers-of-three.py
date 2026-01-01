class Solution:

    def checkPowersOfThree(self, n: int) -> bool:
        remainder=[]
        if n==1:
            return True
        while n>1:
            if n%3==2:
                return False
            n=n//3
        return True

        