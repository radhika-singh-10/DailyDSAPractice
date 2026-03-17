class Solution:
    def myAtoi(self, s: str) -> int:
        sign,res,i,n=1,0,0,len(s)
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        while i<n and s[i] == " ":
            i+=1
        
        if i<n and s[i]=="+":
            sign=1
            i+=1
        elif i<n and s[i]=="-":
            sign=-1
            i+=1
        while i<n and s[i].isdigit():
            digit=int(s[i])
            if (res> INT_MAX // 10) or (res== INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            res=res*10+digit
            i+=1
        return sign*res