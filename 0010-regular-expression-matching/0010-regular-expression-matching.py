class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #if p is empty we nedd to check if s is empty or not-base case
        if not p:
            return not s
        #
        first_match=bool(s) and (p[0] == s[0] or p[0] == ".")#p[0] in {s[0],"."}
        #we will check the occurence ch by ch
        #
        if len(p)>=2 and p[1]=="*":
            return (self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:],p))
        else:
            return first_match and self.isMatch(s[1:],p[1:])