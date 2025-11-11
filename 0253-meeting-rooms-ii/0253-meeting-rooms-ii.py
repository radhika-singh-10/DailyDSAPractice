class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        res,n=1,len(intervals)
        if n==1:
            return 1
        intervals.sort(key=lambda x:x[0])
        heap = []
        for interval in intervals:
            if heap and heap[0]<=interval[0]:
                heappop(heap)
            heappush(heap, interval[1])
        return len(heap)
