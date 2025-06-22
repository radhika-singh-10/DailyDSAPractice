class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n=len(s)
        pos,res,j=dict(),[],n-1
        for i in range(n):
            if s[i].isalpha():
                while not s[j].isalpha():
                    j-=1
                res.append(s[j])
                j-=1
            else:
                res.append(s[i])
        return "".join(res)




        