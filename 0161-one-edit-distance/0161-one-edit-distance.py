class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        #abc abcd
        #ab abc 
        #abdc abcc
        #ec 1 -> either string empty -> return False
        #ec 2 -> if either string is empty and len of other is 1 -> return True
        #lower==lower, upper==upper, digits=digits
        #approach -> to check if whole string is equal, elif after the unequal position, check if equal
        #n,m,i,j=len(s),len(t),0,0
        # if abs(n-m)>1 -> False
        #if s[i]==t[j]->ok
        #elif s[i]!=t[j]
        #   return (s[i+1:]==t[j:] or s[i:]==t[j+1:] or s[i+1:]==t[j+1:])
        if s==t:
            return False
        n,m,i,j=len(s),len(t),0,0
        while i<min(n,m) and s[i]==t[i]:
            i+=1
        return (s[i:]==t[i+1:]) or (s[i+1:]==t[i:]) or (s[i+1:]==t[i+1:])