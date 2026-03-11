class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        if n%2==1:
            return False
        openBrackets,unlocked=0,0
        for i in range(n):
            if locked[i]=="0":
                unlocked+=1
            elif s[i]=="(":
                openBrackets+=1
            elif s[i]==")":
                if openBrackets>0:
                    openBrackets-=1
                elif unlocked>0:
                    unlocked-=1
                else:
                    return False
        balancedCount=0
        for i in range(n-1,-1,-1):
            if locked[i]=="0":
                balancedCount-=1
                unlocked-=1
            elif s[i]=="(":
                openBrackets-=1
                balancedCount+=1
            elif s[i]==")":
                balancedCount-=1
            if balancedCount>0:
                return False
        return True

        # print(openBrackets, unlocked)
        # while openBrackets and unlocked and openBrackets<unlocked:
        #     #print(openBrackets, unlocked, openBrackets[-1], unlocked[-1])
        #     openBrackets-=1
        #     unlocked-=1
        # if openBrackets>0:
        #     return False
        # return True

    