class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #edge case-> one element-> no operation res[0]

        
        #approach->
        #one loop 
        #from i=0to n:
        #from j=i to n: if boxes[i]==1: res[i]+=abs(j-i)
        #from k=n-1 to i:if boxes[i]==1: res[i]+=abs(j-i)

        #tc->0(n^2), sc->0(n)

        n,left_move,right_move=len(boxes),0,0
        answer=[0]*n
        if n==1:
            return answer

        count = 0
        sum = 0
        for i in range(n):
            answer[i] = count * i - sum
            if boxes[i] == '1':
                count += 1
                sum += i
        
        count = 0
        sum = 0

        for i in range(n - 1, -1, -1):
            answer[i] += sum - count * i
            if boxes[i] == '1':
                count += 1
                sum += i
                
        return answer

