class Solution:
    def maximumSwap(self, num: int) -> int:
        if 0<=num<=9:
            return num
        maxElem,secondMaxElem=0,0
        numList=[int(i) for i in str(num)]
        last_occurence = {int(d): i for i, d in enumerate(str(num))}
        for i, digit in enumerate(numList):
            for d in range(9, digit, -1):
                #print(d,digit,i,last_occurence.get(d, -1))
                if last_occurence.get(d, -1) > i:
                    numList[i], numList[last_occurence[d]] = numList[last_occurence[d]], numList[i]
                    return int("".join(map(str, numList)))
        return num

        # for n in numList:
        #     if n>maxElem:
        #         maxElem=n
        #     elif maxElem>n>secondMaxElem:
        #         secondMaxElem=n
        # if numList.index(maxElem)==0:
        #     return num
        # if numList.index(maxElem)!=0:
        #     idx=numList.index(maxElem)
        #     numList[0],numList[idx]=numList[idx],numList[0]
        # # if numList.index(secondMaxElem)!=1:
        # #     idx=numList.index(secondMaxElem)
        # #     numList[1],numList[idx]=numList[idx],numList[1]
        
        # res = int("".join(str(i) for i in numList))
        # return res

        

        # # new_num,cur,idx,j=list(str(num)),0,0,0
        # # for i in range(len(new_num)-1):
        # #         if int(new_num[i])<int(new_num[j]) and cur<int(new_num[j]):
        # #             idx=j
        # #             cur=int(new_num[j])
        # #         j+=1
        # # new_num[i],new_num[idx]=new_num[idx],new_num[i]
        # # res=""
        # # for digit in str(num):
        # #     res+=digit
        # # return int(res) 

        

