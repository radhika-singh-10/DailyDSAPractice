class Solution:
    def countSubstrings(self, s: str) -> int:
        #empty string, len==1->1
        #recursion - 
        #i->0-i(left), j->i,n(right), 
        if not s or len(s)<=1:
            return 1

        n,res=len(s),0
        def checkPalindrome(s,l,r):
            count=0
            while l >= 0 and r < n and s[l] == s[r]:
                print(s[l],s[r])
                count += 1
                l -= 1
                r += 1
            return count


        for i in range(n):
            res+=checkPalindrome(s,i,i)
            res+=checkPalindrome(s,i,i+1)

        return res

