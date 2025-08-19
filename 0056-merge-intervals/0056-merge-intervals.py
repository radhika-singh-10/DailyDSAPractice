class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        mergedIntervals = [intervals[0]]
        for i in range(1,len(intervals)):
            if mergedIntervals[-1][1]>=intervals[i][0]:
                mergedIntervals[-1][1]=max(mergedIntervals[-1][1],intervals[i][1])
            else:
                mergedIntervals.append(intervals[i])
        return mergedIntervals