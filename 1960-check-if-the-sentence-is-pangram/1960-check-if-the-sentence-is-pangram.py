class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #a -> freq[ord(s[i])-ord('a')]+=1
        # freq=[0]*26
        # for i in range(len(sentence)):
        #     freq[ord(sentence[i])-ord('a')]+=1
        # for i in range(26):
        #     if freq[i]==0:
        #         return False
        # return True
        seen_set=set(sentence)
        return len(seen_set)==26
        # for i in range(26):
        #     cur_char=chr(ord('a')+i)
        #     if sentence.find(cur_char)==-1:
        #         return False
        # return True
