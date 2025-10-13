class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res,n=[words[0]],len(words)
        def compare(word1,word2):
            freq=[0]*26
            for ch in word1:
                freq[ord(ch)-ord("a")]+=1
            for ch in word2:
                freq[ord(ch)-ord("a")]-=1
            return all(i==0 for i in freq)
        for i in range(1,n):
            if compare(words[i],words[i-1]):
                continue
            res.append(words[i])
        return res
            
        