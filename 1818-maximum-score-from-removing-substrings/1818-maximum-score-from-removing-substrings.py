class Solution:
    def removeSubstring(self,s,pair):
        stack=[]
        for chr in s:
            if chr==pair[1] and stack and stack[-1]==pair[0]:
                stack.pop()
            else:
                stack.append(chr)
        return "".join(stack)


    def maximumGain(self, s: str, x: int, y: int) -> int:
        higherScoringPair,res=('ab' if x>y else 'ba'),0
        lowerScoringPair=('ba' if higherScoringPair=='ab' else 'ab')
        stringAfterFirstPass=self.removeSubstring(s,higherScoringPair)
        removedPairsCount=(len(s)-len(stringAfterFirstPass))//2
        res+=removedPairsCount*max(x,y)
        stringAfterSecondPass=self.removeSubstring(stringAfterFirstPass,lowerScoringPair)
        removedPairsCount=(len(stringAfterFirstPass)-len(stringAfterSecondPass))//2
        res+=removedPairsCount*min(x,y)
        return res
    
