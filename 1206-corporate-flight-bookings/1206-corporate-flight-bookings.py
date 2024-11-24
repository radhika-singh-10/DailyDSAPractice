class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:   
        #prefix sum question 
        if not bookings:
            return []
        res=[0]*(n+1)
        for first,last,seats in bookings:
            res[first-1]+=seats
            res[last]-=seats
        for j in range(1,n):
            res[j]+=res[j-1]

        return res[:n]
        