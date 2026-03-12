class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        res = 0 
        lo, hi = 0, len(plants)-1
        canA, canB = capacityA, capacityB
        while lo < hi: 
            if canA < plants[lo]: 
                res += 1; canA = capacityA
            canA -= plants[lo]
            if canB < plants[hi]: 
                res += 1; canB = capacityB
            canB -= plants[hi]
            lo, hi = lo+1, hi-1
        if lo == hi and max(canA, canB) < plants[lo]: 
            res += 1
        return res