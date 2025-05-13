class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        n=len(s)
        res=0
        mod = 10**9 + 7
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1
        for round in range(t):
            nxt = [0] * 26
            nxt[0] = freq[25]
            nxt[1] = (freq[25] + freq[0]) % mod
            for i in range(2, 26):
                nxt[i] = freq[i - 1]
            freq = nxt
        ans = sum(freq) % mod
        return ans
        #BRTUE FORCE
        # while t>0:
        #     temp=[ch for ch in s]
        #     new_stack=[]
        #     for idx in range(len(temp)):
        #         if temp[idx]=='z':
        #             new_stack.append('a')
        #             new_stack.append('b')
        #         else:
        #             new_stack.append(chr(ord(temp[idx])+1))
        #     print(new_stack)
        #     s=''.join(new_stack)
        #     t-=1
        # return len(s)

