class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n,m=len(A),len(B)
        res,set_A,set_B=[0]*n,set(),set()
        for i in range(n):
            set_A.add(A[i])
            set_B.add(B[i])
            c=0
            for elem in set_A:
                if elem in set_B:
                    c+=1
            res[i]+=c

        return res
