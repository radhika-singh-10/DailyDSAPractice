class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        n,res=len(word),sys.maxsize
        freq=sorted(Counter(word).values())
        # for i in range(len(freq)):
        #     for v in freq[i:]:
        #         res=min(res,sum(freq[:i])+sum(v-freq[i]-k,0))
        # return res

        return min(sum(freq[:i])+sum(max(v-freq[i]-k,0) for v in freq[i:]) for i in range(len(freq))) 

