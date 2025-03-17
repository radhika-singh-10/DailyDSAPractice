class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n1,n2=len(spells),len(potions)
        res=[0]*n1
        for i in range(n1):
            spell = spells[i]
            l,r=0,n2-1
            while l<=r:
                m=l+(r-l)//2
                product = spell * potions[m]
                if product >= success:
                    r = m - 1
                else:
                    l = m + 1
            res[i] = n2 - l
        return res
                    

        

