class Solution:
    def reverseBits(self, n: int) -> int:
        res,power=0,31
        while n:
            res+=(n&1)<<power
            n=n>>1
            power-=1
        return res





        #convert int to binary representation - string  - and reverse - binary - int

        # sign,num=str(bin(n)).split("b")
        # l=len(num)
        # rev_num=num[::-1]
        
        # #res=sign+'b'+rev_num
        # res=int(rev_num,2)
        # return res
        


        
