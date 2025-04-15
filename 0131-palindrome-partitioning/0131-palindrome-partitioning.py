class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.backtrack(s,[],res)
        return res

    def backtrack(self,s,palindrome,res):
        if not s:
            res.append(palindrome)
            return 
        for i in range(1,len(s)+1):
            #print(s[:i],s[:i][::-1])
            if s[:i]==s[:i][::-1]:
                self.backtrack(s[i:],palindrome+[s[:i]],res)
    
            