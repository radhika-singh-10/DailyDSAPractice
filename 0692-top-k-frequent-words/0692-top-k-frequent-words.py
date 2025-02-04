class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n=[(v,k) for k,v in Counter(words).items()]
        n.sort(key=lambda x:(-x[0],x[1]))
        return [w for f,w in n[:k]]
        # freq=Counter(words)
        # freq=sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        # res = []
        # for word, count in freq:
        #     if len(res) == k:
        #         break
        #     res.append(word)

        # return res



        