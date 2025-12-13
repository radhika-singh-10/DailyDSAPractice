class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        #sliding window  concept - one ptr- fixed , other - moves
        #l->0-n-1
        #r->l+1->n
        occurence, counter = defaultdict(int), 0
        for num in nums:
            counter += occurence[num-k] + occurence[num+k]
            occurence[num] += 1
        return counter