class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n=len(s)
        pos,res,j=dict(),[],n-1
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)
        # #intuition- check if its alpha, and append normally if its not alphabet from backwards, else 
        # for i in range(n):
        #     if s[i].isalpha():
        #         print(res,s[i])
        #         while not s[j].isalpha():
        #             j-=1
        #         res.append(s[j])
        #         j-=1
                
        #     else:
        #         res.append(s[i])
        # return "".join(res)




        