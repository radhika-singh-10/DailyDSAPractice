class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #approach- friends=[i+1 for i in range(n)]
        #till len(friends)==1:
        #
        
        friends=list(range(1, n + 1))
        i=0
        while len(friends)>1:
            j=(i+k-1)%len(friends)
            print(friends,i,j)
            friends.pop(j)
            i=j
            j=0

        return friends[0]


            



            
            

