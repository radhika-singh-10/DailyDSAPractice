class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_num_set=set()
        ugly_num_set.add(1)
        for i in range(n):
            cur_ugly_num = min(ugly_num_set)
            ugly_num_set.remove(cur_ugly_num)
            ugly_num_set.add(2*cur_ugly_num)
            ugly_num_set.add(3*cur_ugly_num)
            ugly_num_set.add(5*cur_ugly_num)
        return cur_ugly_num

        