class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n=len(bills)
        changeMap={5:0,10:0,20:0}
        for i in range(n):
            if bills[i]==5:
                changeMap[bills[i]]+=1
            elif bills[i]==10:
                if changeMap[5]>0:
                    changeMap[5]-=1
                    changeMap[bills[i]]+=1
                else:
                    return False
            else:
                if changeMap[5]>0 and changeMap[10]>0:
                    changeMap[5]-=1
                    changeMap[10]-=1
                    changeMap[bills[i]]+=1
                elif changeMap[5]>=3:
                    changeMap[5]-=3
                    changeMap[bills[i]]+=1

                else:
                    return False

        return True
            
            
            
