class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #backtrack to contain all the permutaiton in record 
        #get k-1 index permutation from the record and return
        used = [False] * n
        result = []
        count = [0]  

        def backtrack(path):
            if len(path) == n:
                count[0] += 1
                if count[0] == k:
                    result.append(''.join(path))
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(str(i + 1))
                    backtrack(path)
                    path.pop()
                    used[i] = False
                    if result:
                        return  
        backtrack([])
        return result[0]