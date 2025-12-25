class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time==0:
            return [idx for idx in range(0,len(security))]
        res=[]
        n=len(security)
        non_incr_left,non_decr_right=[0]*n,[0]*n
        for i in range(1,n):
            if security[i-1]>=security[i]:
                non_incr_left[i]=non_incr_left[i-1]+1
                continue
        for i in range(n-2,-1,-1):
            if security[i]<=security[i+1]:
                non_decr_right[i]=non_decr_right[i+1]+1
                continue
        #print(non_incr_left,non_decr_right)
        for i in range(time,n-time):
            #print(i,non_incr_left[i],non_decr_right[i])
            if non_incr_left[i]>=time and non_decr_right[i]>=time:
                res.append(i)
        return res
