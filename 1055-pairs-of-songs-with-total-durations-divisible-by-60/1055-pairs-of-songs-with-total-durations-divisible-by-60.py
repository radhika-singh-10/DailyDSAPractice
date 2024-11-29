class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res=0
        #30,20,150,100,40 | 60,60,60
        #brute force->time limit exceeded->o(n^2),0(1)
        remainder=defaultdict(int)
        for t in time:
            if t%60==0:  #30,20,150
                res+=remainder[0] #150
            else:
                res+=remainder[(60-t)%60] #30,20
            remainder[t%60]+=1 
        return res