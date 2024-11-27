class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        #upper and lower case->diff, no leading or training spaces
        #circular sentence
        #last char of 1st word=first char of next word
        #last char of 1st word=first char of first word

        #edge cases - empty string -> true, 
        #1 word-> last char==1st char
        #appraoch -> 
        #sperate by comma -> fill in the list, 
        #search and check 
        #first word,first char=last word, last char
        #loop->check the last word(i-1)[-1], last char== next word,first char(i)[0]

        if len(sentence)<=1:
            return True
        words=sentence.split()
        if len(words)==1:
            return True if words[0][0]==words[0][-1] else False
        for i in range(len(words)-1):
            if words[i][-1]!=words[i+1][0]:
                return False
        return True if words[len(words)-1][-1]==words[0][0] else False

                
