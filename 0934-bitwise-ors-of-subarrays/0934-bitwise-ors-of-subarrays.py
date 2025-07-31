class Solution:

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res,prev = set(),set()
        for num in arr:
            cur = {num}
            for p in prev:
                cur.add(p | num)
            prev = cur
            res |= cur
            
        return len(res)