class Solution:
    def integerReplacement(self, n: int) -> int:
        
        def divide(num):
            if num==1:
                return 0
            if num%2==0:
                return 1+divide(num//2)
            else:
                return 1+min(divide(num+1),divide(num-1))
            
        
        return divide(n)
        
