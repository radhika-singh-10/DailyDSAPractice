class Solution:
    def clearStars(self, s: str) -> str:
        n,res,deleted,heap=len(s),[],set(),[]
        #lowercase only or uppercase present
        #no * -> same s as response
        #only * -> return empty string
        #if * at 1st index-> invalid index
        for i,ch in enumerate(s):
            if ch=='*':
                c,neg=heapq.heappop(heap)
                deleted.add(-neg)
            else:
                heapq.heappush(heap,(ch,-i))
        for i,ch in enumerate(s):
            if i in deleted or ch == '*': 
                continue
            res.append(ch)
        return ''.join(res)