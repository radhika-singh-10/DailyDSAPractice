class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(cur,temp,index,n):
            #temp.sort()
            if cur==0:
                #if temp not in res:
                res.append(temp.copy())
            elif cur<0:
                return 

            for i in range(index,n):
                temp.append(candidates[i])
                backtrack(cur-candidates[i],temp,i,n)
                temp.pop()
                



        res,n=[],len(candidates)
        backtrack(target,[],0,n)        
        return res


