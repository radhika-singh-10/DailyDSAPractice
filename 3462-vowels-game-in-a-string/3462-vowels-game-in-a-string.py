class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel_count = 0
    
        for i in s:
            if i in 'aeiou':
                return True
        return False