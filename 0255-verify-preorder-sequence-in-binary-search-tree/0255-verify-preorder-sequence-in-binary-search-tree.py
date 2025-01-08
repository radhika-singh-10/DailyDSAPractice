from collections import deque
import sys
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        #convert preorder to inorder which is an increasing monostatic stack
        #and check if its increasing or not 
        #if the stack is empty then true, else false
        #0(n), 0(n)

        stack,res=[],False
        min_num = -sys.maxsize
        for i in range(len(preorder)):
            while stack and stack[-1]<=preorder[i]:
                min_num=stack.pop()
                
            # if not stack and i==len(preorder)-1:
            #     return True

            if preorder[i] <= min_num:
                return False

            stack.append(preorder[i])

        return True
            
