class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #we need to iterate i by keeping las 0 and r as n-1 always
        res,n=[],len(s)
        # dp=[[False]*n for _ in range(n)]
        # self.backtrack(s,[],0,res,dp)
        self.backtrack(s,[],res)
        return res
    # def backtrack(self,s,palindrome,i,res,dp):
    #     if i>=len(s):
    #         res.append(list(palindrome))
    #     for j in range(i,len(s)):
    #         if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
    #             dp[i][j]=True
    #             palindrome.append(s[i:j+1])
    #             self.backtrack(s,palindrome,j+1,res,dp)
    #             palindrome.pop()
    def backtrack(self,s,palindrome,res):
        if not s:
            res.append(palindrome)
            return 
        for i in range(1,len(s)+1):
            print(i,s[:i],s[:i][::-1],s,palindrome,s[i:])
            if s[:i]==s[:i][::-1]:
                self.backtrack(s[i:],palindrome+[s[:i]],res)
    
            