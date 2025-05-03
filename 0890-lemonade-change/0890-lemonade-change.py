class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n=len(bills)
        fiveChange,tenChange=0,0
        # changeMap={5:0,10:0,20:0}
        for i in range(n):
            if bills[i]==5:
                fiveChange+=1
            elif bills[i]==10:
                if fiveChange>0:
                    fiveChange-=1
                    tenChange+=1
                else:
                    return False
            else:
                if fiveChange>0 and tenChange>0:
                    fiveChange-=1
                    tenChange-=1
                    # changeMap[bills[i]]+=1
                elif fiveChange>=3:
                    fiveChange-=3
                    # changeMap[bills[i]]+=1

                else:
                    return False

        return True
            
            
            
