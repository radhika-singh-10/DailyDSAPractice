class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        bo={'electronics':0,'grocery':1,'pharmacy':2,'restaurant':3,'invalid':4}
        sc=sorted(zip(businessLine,code,isActive),key=lambda x:(bo[x[0]],x[1],x[2]))
        ans=[]
        for b,c,a in sc:
            if a and b!='invalid' and c.replace('_','a').isalnum():
                ans.append(c)
        return ans
        # n=len(code)
        # res=[]
        # for i in range(n):
        #     # print(i)
        #     # print((code[i].isalnum() or code[i].__contains__('_')))
        #     # print((businessLine[i]=="electronics" or businessLine[i]=="grocery" or businessLine[i]== "pharmacy" or businessLine[i]== "restaurant"))
        #     # print(isActive[i])
        #     if (code[i].isalnum() or code[i].__contains__('_')) and (businessLine[i]=="electronics" or businessLine[i]=="grocery" or businessLine[i]== "pharmacy" or businessLine[i]== "restaurant") and isActive[i]:
        #         res.append(code[i])
        # return sorted(res)