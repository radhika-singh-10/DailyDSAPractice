class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = defaultdict(int)
        for x in deliciousness: 
            freq[x] += 1
        res = 0
        for x in freq: 
            for k in range(22): 
                if 2**k - x <= x and 2**k - x in freq: 
                    res += freq[x]*(freq[x]-1)//2 if 2**k - x == x else freq[x]*freq[2**k-x]
        return res % 1000000007