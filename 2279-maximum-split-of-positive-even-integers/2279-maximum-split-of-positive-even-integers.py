class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        #backtracking concept - i,n-i -> these nos are even 
        #if nis odd-> return empty
        #else check from 2 index till finalSum, if it matches the condition and increment by 2
        if finalSum % 2!=0:
            return []
        self.res = []
        self.backtrack(finalSum,0,[],2)
        return self.res
        
    def backtrack(self, finalSum, curSum, temp, start):
        if curSum == finalSum and len(temp) > len(self.res):
            self.res=temp
            return True
            
        for i in range(start, finalSum+1, 2):
            if curSum + i > finalSum:
                break
            temp.append(i)
            if self.backtrack(finalSum, curSum + i,temp, i+2):
                return True
            temp.pop()
        
    