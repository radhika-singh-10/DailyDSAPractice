class Solution:
    def isNumber(self, s: str) -> bool:
        #questions of conditions - think of edge cases in a solution
        # seen_digit = seen_exponent = seen_dot = False
        exponent,digit,dot=False,False,False
        n=len(s)
        for i,c in enumerate(s):
            if c.isdigit():
                digit=True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e","E"]:
                if exponent or not digit:
                    return False
                exponent=True
                digit=False
            elif c==".":
                # if i==n-1 and digit:
                #     return True
                if dot or exponent:
                    return False
                dot=True
                
            else:
                return False
        return digit
