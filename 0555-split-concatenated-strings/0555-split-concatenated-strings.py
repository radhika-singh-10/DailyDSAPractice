class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        

        newString=[s if s>=s[::-1] else s[::-1] for s in strs]
        res=''
        for i,s in enumerate(newString):
            for s2 in [s,s[::-1]]:
                for j in range(len(s2)):
                    cur=s2[j:]+''.join(newString[i+1:]+newString[:i])+s2[:j]
                    res=max(res,cur)
        return res


