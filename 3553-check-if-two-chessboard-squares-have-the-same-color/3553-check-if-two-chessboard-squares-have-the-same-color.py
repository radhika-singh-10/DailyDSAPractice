class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        s1 = (ord(coordinate1[0]) - ord('a')) + int(coordinate1[1])
        s2 = (ord(coordinate2[0]) - ord('a')) + int(coordinate2[1])
        return s1 % 2 == s2 % 2
            
