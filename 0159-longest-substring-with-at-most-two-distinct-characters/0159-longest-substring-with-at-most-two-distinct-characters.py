class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_map = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            char_map[s[r]] = char_map.get(s[r], 0) + 1
            
            while len(char_map) > 2:
                char_map[s[l]] -= 1
                if char_map[s[l]] == 0:
                    del char_map[s[l]]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res