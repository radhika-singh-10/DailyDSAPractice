from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right : right + word_length]
                if sub not in word_count:
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length  
                else:
                    while right - left == substring_size or excess_word:
                        leftmost_word = s[left : left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if (
                            words_found[leftmost_word]
                            == word_count[leftmost_word]
                        ):
                            excess_word = False
                        else:
                            words_used -= 1
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        excess_word = True

                    if words_used == k and not excess_word:
                        answer.append(left)

        answer = []
        for i in range(word_length):
            sliding_window(i)

        return answer
        







        #using backtracking i can create all combinations of words list
        #and need to apply sliding window in order to check over the combinations of substring if they exist then add their starting indices in the result
        #brute force approach
        # combinations,n,res=[],len(words),set()
        # def backTrack(words,combinations,stack,s):
        #     if not words and stack in s:
        #         combinations.append(stack)
        #         return
        #     n = len(words)
        #     for i in range(n):
        #         backTrack(words[:i]+words[i+1:],combinations,stack+words[i],s)

        # backTrack(words,combinations,"",s)

        # print(combinations)
        # n,m=len(s),len(combinations)
        # l=0
        # # for word in range(m):
        # #     if word in s:

        # # for r in range(n):
        # #     while r<n and words[l:r+1] not in combinations:
        # #         r=r+1
        # #     res.add(l)
        # #     r+=1
        # #     l=r
        # if combinations:
        #     l=len(combinations[0])
            
        #     for i in range(n):

        #         if s[i:i+l] in combinations:
        #             res.add(i)
                


                



        # return list(res)




