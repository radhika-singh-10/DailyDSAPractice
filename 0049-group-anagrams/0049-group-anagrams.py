class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        # for s in strs:
        #     res[tuple(sorted(s))].append(s)
        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            res[tuple(count)].append(word)

        return list(res.values())
  