class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        # fruits.sort(reverse=True)
        # baskets.sort(reverse=True)
        placement=0#[False]*n
        for i in range(n):
            for j in range(n):
                if fruits[i]<=baskets[j]:
                    placement+=1
                    baskets[j]=-1
                    break
        return n-placement
        #     while j<n and fruits[i]>baskets[j]:
        #         j=j+1
        #     if j<n:
        #         placement[i]=True
        # return placement.count(False)
            

            # if fruits[i]<=baskets[i]:
            #     baskets[i]-=fruits[i]
            #     fruits[i]=0
            # else:
            #     fruits[i]-=baskets[i]
                
        return sum(fruits)
        

