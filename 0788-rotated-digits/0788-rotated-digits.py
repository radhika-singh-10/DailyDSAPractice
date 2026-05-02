class Solution:
    def rotatedDigits(self, n: int) -> int:
        good_digits = {2: 5,5: 2,6: 9,9: 6}
        same_digits = {0, 1, 8}
        res = 0

        for num in range(1, n + 1):
            num_str = list(str(num))
            valid = True
            for idx, ch in enumerate(num_str):
                digit = int(ch)

                if digit in good_digits:
                    num_str[idx] = str(good_digits[digit])
                elif digit in same_digits:
                    continue
                else:
                    valid = False
                    break

            rotated_num = int("".join(num_str))

            if valid and rotated_num != num:
                res += 1

        return res
                    
