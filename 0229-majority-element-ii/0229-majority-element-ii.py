from collections import Counter, defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #edge cases - same elements, no elem, 1 elem
        #appraoch
        #[3,2,3] - freq= {3:2, 2:1} , floor(n/3)=1 freq[0]==1

        #tc-0(n), sc=0(n)
        freq=Counter(nums)
        n=len(nums)
        res=[]
        for i in freq:
            if freq[i]>floor(n/3):
                res.append(i)

        return res


        