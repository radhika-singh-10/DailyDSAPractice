class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary=""
        while n>0:
            binary+=str(n%2)
            n//=2
        status=False
        for i in range(len(binary)-1):
            if binary[i]==binary[i+1]:
                return False
        return True


        
