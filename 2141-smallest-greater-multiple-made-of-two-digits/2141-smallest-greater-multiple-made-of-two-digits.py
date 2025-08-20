class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        if digit1==0 and digit2==0 and max(digit1,digit2)<k:
            return -1
        upperLimit = 2**31
        #perform a search - thinking of dfs/bfs
        minVal, maxVal = min(digit1,digit2), max(digit1,digit2)
        stack,visited=[],set()
        for val in [minVal,maxVal]:
            stack.append(val)
            visited.add(val)
        print(stack,visited)
        while stack:
            cur=stack.pop(0)
            if cur>k and cur%k==0:
                return cur
            for num in [minVal,maxVal]:
                newVal=cur*10+num #0,2, 2, 20, 22
                #0, 7,70, 77, 700, 777
                #print(stack,visited,newVal,cur,num)
                if newVal not in visited and newVal<upperLimit:
                    stack.append(newVal)
                    visited.add(newVal)
        return -1
                    


        return -1


        # digits={digit1,digit2}
        # res=-1
        #
        # for n in range(k+1,upperLimit):
        #     temp=n
        #     flag=True
        #     while temp>0:
                
        #         if (temp%10) not in digits:
        #             flag=False
        #             break
        #         temp//=10
                
        #     if flag and n%k==0:
        #         res=n
        #         break
        # return res
            


