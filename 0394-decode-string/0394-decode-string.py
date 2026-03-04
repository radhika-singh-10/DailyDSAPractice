class Solution:
    def decodeString(self, s: str) -> str:
        stack,num,res=[],0,""
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i]=='[':
                stack.append(res)
                stack.append(num)
                res=""
                num=0
            elif s[i]==']':
                temp_num=stack.pop()
                temp_str=stack.pop()
                res = temp_str +temp_num*res
            else:
                res+=s[i]
            
        return res