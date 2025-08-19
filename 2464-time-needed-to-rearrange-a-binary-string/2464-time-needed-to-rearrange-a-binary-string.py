class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n=len(s)
        zeroes = ones = ans = 0
        for c in s:
            if c == "1":
                if zeroes:
                    ans = max(ans+1,zeroes)
                ones+=1
            else:
                zeroes+=1
        return ans
        # brute force
        # res=0
        # while '01' in s:
        #     s=s.replace('01','10')
        #     res+=1
        # return res
        