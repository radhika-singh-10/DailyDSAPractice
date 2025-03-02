from collections import deque
#approach -> stack=[], while stack and i<0<stack[-1]: if abs(i) >stack[-1]: stack.pop() elif abs(i)==res[-1] break
#else append(i)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #one astreoids- return the eleme
        #more than one
        #- push into a stack, and get the top two elems 
        # i. if prod>0 -> same direction-no hcange
        # ii. elif prod<0 -> if the abs(val) same, pop both 
        #                 -> else remove the smaller elem (abs val)


        stack = []

        for asteroid in asteroids:
            flag=True
            while stack and asteroid*stack[-1]<0 and asteroid<0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                flag=False
                break
            if flag:
                stack.append(asteroid)

        return stack



        
        