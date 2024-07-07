class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res=0
        for i in range(1,len(colors)-1):
            if colors[i]!=colors[i-1] and colors[i]!=colors[i+1]:
                res+=1   
        if colors[0] != colors[1] and colors [0]!=colors[-1]:
            res +=1
        if colors[-2]!=colors[-1] and colors [-1]!=colors[0]:
            res +=1
        return res