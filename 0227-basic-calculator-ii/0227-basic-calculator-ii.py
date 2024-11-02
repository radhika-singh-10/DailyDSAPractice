class Solution:
    def calculate(self, s: str) -> int:
        stack,op,cur,n=[],"+",0,len(s)
        for i in range(n):
            if s[i].isdigit():
                cur=cur*10+int(s[i])
            if s[i] in "+-*/" or i==len(s)-1:
                if op=="+":
                    stack.append(cur)
                elif op=="-":
                    stack.append(-cur)
                elif op=="*":
                    stack[-1]=stack[-1]*cur
                elif op=="/":
                    stack[-1]=int(stack[-1]/cur)
                
                op=s[i]
                cur=0

        return sum(stack)


        
        # n,new_s=len(s),[]
        # for i in range(n-1,0,-1):
        #     if s[i]!=" ":
        #         new_s.append(s[i])

        # res=0
        # while len(new_s)>0:
        #     while new_s.__contains__("/"):
        #         index=new_s.index("/")
        #         res=res*10+int(new_s[index-1])//int(new_s[index+1])
        #         new_s.remove(index)
        #         new_s.remove(index)
        #         new_s.remove(index-1)

        #     while new_s.__contains__("*"):
        #         index=new_s.index("*")
        #         res=res*10+int(new_s[index-1])*int(new_s[index+1])
        #         new_s.remove(index)
        #         new_s.remove(index)
        #         new_s.remove(index-1)

        #     while new_s.__contains__("+"):
        #         index=new_s.index("+")
        #         res=res*10+int(new_s[index-1])+int(new_s[index+1])
        #         new_s.remove(index)
        #         new_s.remove(index)
        #         new_s.remove(index-1)

        #     while new_s.__contains__("-"):
        #         index=new_s.index("-")
        #         res=res*10+int(new_s[index-1])-int(new_s[index+1])
        #         new_s.remove(index)
        #         new_s.remove(index)
        #         new_s.remove(index-1)

        # return res