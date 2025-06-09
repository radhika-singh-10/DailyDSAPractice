class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        #trie tree - prefix search
        
        curr=1
        k-=1
        while k>0:
            steps=self.countSteps(n,curr,curr+1)
            print(k,steps)
            if steps<=k:
                curr+=1
                k-=steps
            else:
                curr*=10
                k-=1
        return curr


    def countSteps(self,n,prefOne,prefTwo):
        steps=0
        while prefOne<=n:
            steps+=min(n+1,prefTwo)-prefOne
            prefOne*=10
            prefTwo*=10
        return steps
        

