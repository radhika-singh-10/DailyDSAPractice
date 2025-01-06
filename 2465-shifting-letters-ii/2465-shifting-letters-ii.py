class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        shift=[0]*(n+1)
        for start, end, direction in shifts:
            if direction == 0: 
                shift[start] -= 1
                shift[end + 1] += 1
            else: 
                shift[start] += 1
                shift[end + 1] -= 1

        for i in range(1, n):
            shift[i] += shift[i - 1]

        res = []
        for i in range(n):
            normalized_shift = (shift[i] % 26 + 26) % 26
            new_char = chr((ord(s[i]) - ord('a') + normalized_shift) % 26 + ord('a'))
            res.append(new_char)

        return ''.join(res)

