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

        prefix_count = 0
        prefix_sum = 0
        for i in range(n):
            answer[i] = prefix_count * i - prefix_sum
            if boxes[i] == '1':
                prefix_count += 1
                prefix_sum += i
        
        suffix_count = 0
        suffix_sum = 0

        for i in range(n - 1, -1, -1):
            answer[i] += suffix_sum - suffix_count * i
            if boxes[i] == '1':
                suffix_count += 1
                suffix_sum += i
                
        return answer

