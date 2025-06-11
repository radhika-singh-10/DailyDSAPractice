class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - minEven        
        # freq=Counter(s)
        # maxOddFreq,minOddFreq,maxEvenFreq,minEvenFreq=0,0,0,0
        # for i in range(len(freq)):
        #     if freq[i]%2!=0:
        #         maxOddFreq=max(maxOddFreq,i)
        #         minOddFreq=min(minOddFreq,i)
        #     else:
        #         minEvenFreq=min(minEvenFreq,i)
        #         maxEvenFreq=max(maxEvenFreq,i)
        # return max(abs(maxOddFreq-minEvenFreq),abs(maxEvenFreq-minOddFreq))

            
