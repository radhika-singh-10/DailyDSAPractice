class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="[" or i=="{" or i=="(":
                stack.append(i)
            elif (i=="]" and len(stack)>0 and stack[-1]=="[") or (i=="}" and len(stack)>0 and stack[-1]=="{") or (i==")" and len(stack)>0 and stack[-1]=="("):
                v=stack.pop()
            else:
                stack.append(i)
            

        return not stack
        