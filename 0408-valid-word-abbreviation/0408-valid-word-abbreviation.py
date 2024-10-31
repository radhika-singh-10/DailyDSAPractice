class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n1, n2 = len(word), len(abbr)
        i = j = 0  
        
        while i < n1 and j < n2:
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                count = 0
                while j < n2 and abbr[j].isdigit():
                    count = count * 10 + int(abbr[j])
                    j += 1
                i += count 
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        return i == n1 and j == n2
