import sys
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n,res,count,price_sum=len(costs),0,0,0
        for i in range(n):
            if coins<price_sum+costs[i]:
                break
            else:
                price_sum+=costs[i]
                count+=1
        return count
                

