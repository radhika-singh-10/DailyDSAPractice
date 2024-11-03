class Solution:
    def isBalanced(self, num: str) -> bool:
        res,odd_sum,even_sum=False,0,0
        for i in range(len(num)):
            if i%2==0:
                even_sum+=int(num[i])
            else:
                odd_sum+=int(num[i])

        return True if odd_sum==even_sum else False
            