class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1=[0]*26
        for i in range(len(s)):
            c1[ord(s[i])-ord('a')]+=1
            c1[ord(t[i])-ord('a')]-=1

        for i in range(len(c1)):
            if c1[i] != 0:
                return False

        return True