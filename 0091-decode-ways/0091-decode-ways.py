class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        num,n=int(s),len(s)
        count=set()
        l,r=0,len(s)-1
#         hm={
#             "A":1,"B":2,"C":3,"D":4,"E":5,"F":6
# ,"G":7,"H":8 ,"I":9 ,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26     }
        dp=[0]*(n+1)
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            ones=int(s[i-1])
            twos=int(s[i-2:i])
            if ones!=0:
                dp[i]+=dp[i-1]
            if twos>=10 and twos<=26:
                dp[i]+=dp[i-2]

        return dp[n]





        return num