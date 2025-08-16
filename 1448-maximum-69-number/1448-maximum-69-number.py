class Solution:
    def maximum69Number (self, num: int) -> int:
        #is 6 is before 9 swap-2pointer
        stack=list(str(num))
        maxNum=num
        for i in range(len(stack)):
            if stack[i] in ('6', '9'):
                flipped = '9' if stack[i] == '6' else '6'
                candidate = int("".join(stack[:i] + [flipped] + stack[i+1:]))
                maxNum = max(maxNum, candidate)

        return maxNum
