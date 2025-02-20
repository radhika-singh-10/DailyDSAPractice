from functools import lru_cache

class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        #time complexity will be o(logn) else it was 0(n)
        #space complexity will be 0(logn)
        def divide(num):
            if num==1:
                return 0
            if num%2==0:
                return 1+divide(num//2)
            else:
                return 1+min(divide(num+1),divide(num-1))
            
        
        return divide(n)
        
