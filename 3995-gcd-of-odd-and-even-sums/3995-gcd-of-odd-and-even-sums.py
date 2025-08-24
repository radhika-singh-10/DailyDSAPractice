class Solution:
    def gcd(self,num1,num2):
        if num1>num2:
            gcd(num2,num2%num1)
        else:
            gcd(num1%num2,num2)
        return num1//num2 if num1>num2 else num2//num1

        
        
    def gcdOfOddEvenSums(self, n: int) -> int:
        evenSum,oddSum=n*(n+1),n*n
        return math.gcd(evenSum,oddSum)
        # count,oddSum,evenSum,num=2*n,n*n,n*(n+1),1
        # while count>0:
        #     if num%2==0:
        #         evenSum+=num
        #     else:
        #         oddSum+=num
        #     num+=1
        #     count-=1
        return gcd(evenSum,oddSum)
        