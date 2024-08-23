import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        res,sieve,min_diff=[-1,-1],[True]*(right+1),math.inf
        sieve[0],sieve[1]=False,False
        for i in range(2,int(math.sqrt(right)+1)):
            if sieve[i]:
                for j in range(i*i,right+1,i):
                    sieve[j]=False
        primes=[i for i in range(left,right+1) if sieve[i]]
        for i in range(len(primes)-1):
            diff=primes[i+1]-primes[i]
            if diff<min_diff:
                min_diff=diff
                res[0],res[1]=primes[i],primes[i+1]

        return res


