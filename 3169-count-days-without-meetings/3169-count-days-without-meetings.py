class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res,prev_end = 0,0
        for start, end in meetings:
            if start > prev_end + 1:
                res += start - prev_end - 1
            prev_end = max(prev_end, end)
        res += days - prev_end
        return res

