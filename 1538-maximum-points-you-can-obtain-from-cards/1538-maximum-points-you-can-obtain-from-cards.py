class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n,res=len(cardPoints),0
        # prefix_sum,suffix_sum=[0]*n,[0]*n
        # prefix_sum[0],suffix_sum[-1]=cardPoints[0],cardPoints[-1]
        # for i in range(1,n):
        #     prefix_sum[i]+=prefix_sum[i-1]+cardPoints[i]
        #     #print(cardPoints[i],i,prefix_sum[i-1],prefix_sum[i])
        # for i in range(n-2,-1,-1):
        #     suffix_sum[i]+=suffix_sum[i+1]+cardPoints[i]
        
        #     #print(cardPoints[i],i)
        # print(prefix_sum,suffix_sum)
        # return max(prefix_sum[k-1],suffix_sum[n-k])

        #max should be attained by taking max elements from either side
        #so we should go for dp
        #brute force solution
        # res=0
        # def getMax(cardPoints,left,right,k):
        #     if left==n-1 or right==0 or k==0:
        #         return 0
        #     return max(cardPoints[left]+getMax(cardPoints,left+1,right,k-1),
        #         cardPoints[right]+getMax(cardPoints,left,right-1,k-1))
        # if k==0:
        #     return 0
        # elif k>=n:
        #     return sum(cardPoints)
        # return getMax(cardPoints,0,n-1,k)

        #prefixsuffix
        front,rear=[0]*(k+1),[0]*(k+1)
        for i in range(k):
            front[i+1]=front[i]+cardPoints[i]
            rear[i+1]=rear[i]+cardPoints[n-1-i]

        for i in range(k+1):
            res=max(front[i]+rear[k-i],res)
        return res




        
