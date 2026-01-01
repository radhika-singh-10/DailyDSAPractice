class Solution:
    def isPowerOfThree(self,power,num):
        if num==0 :
            return True
        if 3**power>num:
            return False
        addPower=self.isPowerOfThree(power+1,num-3**power)
        skipPower=self.isPowerOfThree(power+1,num)
        return addPower or skipPower

        
    def checkPowersOfThree(self, n: int) -> bool:
        remainder=[]
        if n==1:
            return True
        return self.isPowerOfThree(0,n)
        