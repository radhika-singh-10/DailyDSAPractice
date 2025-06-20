class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # dirs,res={'N':[0,1],'S':[0,-1],'E':[1,0],'W':[-1,0]},0
        # sArr=[i for i in s]
        # for i in range(1,len(s)):
        #     if k==0:
        #         break
        #     if (sArr[i]=='N'and sArr[i]=='S') or (sArr[i]=='S'and sArr[i]=='N') ) and k>0:
        #     # if (abs(dirs[sArr[i][0]])==abs(dirs[sArr[i-1][0]]) or abs(dirs[sArr[i][1]])==abs(dirs[sArr[i-1][1]])) and k>0:
        #         sArr[i]=sArr[i-1]

        # for i in range(len(sArr)):
        #     res=max(res,abs(dirs[sArr[i][0]]+dirs[sArr[i][1]]))
        # return res
        res,latitude,longitude,n=0,0,0,len(s)
        for i in range(n):
            if s[i]=='N':
                latitude+=1
            elif s[i]=='S':
                latitude-=1
            elif s[i]=='E':
                longitude+=1
            elif s[i]=='W':
                longitude-=1
            res=max(res,min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return res
            


            


