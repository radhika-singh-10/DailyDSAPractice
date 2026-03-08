class Solution:
    def decodeString(self, s: str) -> str:
        stack,num,res=[],0,""
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i]=='[':
                stack.append(num)
                stack.append(res)
                
                res=""
                num=0
            elif s[i]==']':
                temp_str=stack.pop()
                temp_num=stack.pop()
                res = temp_str +temp_num*res
            else:
                res+=s[i]
            
        return res