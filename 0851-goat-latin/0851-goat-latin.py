class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        add_one,add_two,count,str_ls="ma","a",len(sentence.split(" ")),sentence.split(" ")
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res=""
        for i in range(len(str_ls)):
            word = str_ls[i]
            if word[0].lower() in vowels:
                res += word + "ma"
            else:
                res += word[1:] + word[0] + "ma"
            res += "a" * (i + 1)
        
            if i < len(str_ls) - 1:
                res += " "

        return res