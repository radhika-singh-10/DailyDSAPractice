class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        #[1,1,2,5,6,7,10]
        res,n=set(),len(candidates)
        def generate_combinations(i,total,temp):
            if total==target:
                res.add(tuple(temp))
            if n==i or total>target:
                return 
            temp.append(candidates[i])
            generate_combinations(i+1,total+candidates[i],temp)
            temp.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            generate_combinations(i+1,total,temp)

        generate_combinations(0,0,[])
        return [combination for combination in res]
        



