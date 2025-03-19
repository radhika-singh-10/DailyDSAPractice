class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}
        #0-n-k index
        res,n,count=0,len(s),0
        for i in range(k):
            count+=int(s[i] in vowels)

        res=count
        for i in range(k,n):
            count+=int(s[i] in vowels)
            count-=int(s[i-k] in vowels)
            res=max(res,count)

        return res