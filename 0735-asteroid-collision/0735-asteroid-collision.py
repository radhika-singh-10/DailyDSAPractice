from collections import deque
#approach -> stack=[], while stack and i<0<stack[-1]: if abs(i) >stack[-1]: stack.pop() elif abs(i)==res[-1] break
#else append(i)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for i in asteroids:
            while res and i*res[-1]<0 and i<0:
                if abs(i) > res[-1]:
                    res.pop()
                    continue
                elif abs(i) == res[-1]:
                    res.pop()
                break
            else:
                res.append(i)

        return res



        
        