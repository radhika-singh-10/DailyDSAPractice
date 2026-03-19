class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack=[]
        for i in range(len(nums)):
            
            while k>0 and stack and stack[-1]>nums[i]:
                stack.pop()
                k-=1
            stack.append(nums[i])
        # if stack[0]=="0" and len(stack)>1:
        #     return "".join(stack[1:])
        while k>0:
            stack.pop()
            k-=1

        res=''.join(stack).lstrip('0')
        return res if res else "0"
            
