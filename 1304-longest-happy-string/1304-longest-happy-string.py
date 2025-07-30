class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq,res = [],[]
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        print(pq)
        while pq:
            count, chr = heapq.heappop(pq)
            count = -count
            if (len(res)>=2 and res[-1]==chr and res[-2]==chr):
                if not pq:
                    break
                tempCount,tempChr = heapq.heappop(pq)
                res.append(tempChr)
                if (tempCount+1)<0:
                    heapq.heappush(pq,(tempCount+1,tempChr))
                heapq.heappush(pq,(-count,chr))
            else:
                count-=1
                res.append(chr)
                if count>0:
                    heapq.heappush(pq,(-count,chr))
        return "".join(res)
