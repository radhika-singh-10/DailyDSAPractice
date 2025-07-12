from collections import Counter

class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:        
        n = len(s)
        if n < count:
            return 0
        res = 0

        for i in range(1, 27):  
            freq = Counter()
            unique = 0
            l = 0
            for r in range(n):
                freq[s[r]] += 1
                if freq[s[r]] == count:
                    unique += 1
                if r - l + 1 > i * count:
                    if freq[s[l]] == count:
                        unique -= 1
                    freq[s[l]] -= 1
                    l += 1
                if r - l + 1 == i * count and unique == i:
                    res += 1
        return res