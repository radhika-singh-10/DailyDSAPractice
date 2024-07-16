import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_one=datetime.datetime.strptime(date1,'%Y-%m-%d').date()
        date_two=datetime.datetime.strptime(date2,"%Y-%m-%d").date()
        return abs((date_one-date_two).days)