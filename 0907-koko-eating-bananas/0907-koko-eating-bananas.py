class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<r:
            m=(l+r)//2
            hr_sp=0
            for pile in piles:
                hr_sp+=math.ceil(pile/m)
            if hr_sp<=h:
                r=m
            else:
                l=m+1

        return r

        