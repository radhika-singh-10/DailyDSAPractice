class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets,n,l={},len(fruits),0
        #sliding window - get max continuous len without breaking
        for r,fruit in enumerate(fruits):
            baskets[fruit]=baskets.get(fruit,0)+1
            if len(baskets)>2:
                baskets[fruits[l]]-=1
                if baskets[fruits[l]]==0:
                    del baskets[fruits[l]]
                l+=1
        return r-l+1


