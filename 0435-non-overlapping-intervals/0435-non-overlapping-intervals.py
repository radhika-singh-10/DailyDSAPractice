class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) 
        res = intervals[0][1] 
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= res:
                res = intervals[i][1]
            else:
                count+=1

        return count
