class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        #edge cases->empty word list/query list-> empty result?
        #if r> len(word[i])?? len(word) is final?
        #if l>len(word[i])??return 0 ?
        #
        #approach
        #store the sum of vowels present in the words at each index
        # prefix_sum[i]=prefix_sum[queries[i][0]]-prefixSum[quueries[i][1]]

        
        res,count=[],0
        vowel_ls=['a','e','i','o','u']
        prefix_sum = [0] * len(words)
        for i in range(len(words)):
            cur=words[i]
            if cur[0] in vowel_ls and cur[-1] in vowel_ls:
                count+=1
            prefix_sum[i]=count
        for cur in queries:
            start, end = cur[0], cur[1]
            if start == 0:
                res.append(prefix_sum[end])
            else:
                res.append(prefix_sum[end] - prefix_sum[start - 1])
        
        return res
                        



        