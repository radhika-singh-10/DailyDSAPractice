class Solution:
    def decodeString(self, s: str) -> str:
        stack,num,res=[],0,""
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i=='[':
                stack.append(res)
                stack.append(num)
                res=""
                num=0
            elif i==']':
                temp_num=stack.pop()
                temp_str=stack.pop()
                res = temp_str +temp_num*res
            else:
                res+=i
            
        return res
            