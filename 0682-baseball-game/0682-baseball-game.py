class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack,res,prev_record=[],0,0
        for i in range(len(operations)):
            if operations[i]=="+" and len(stack)>=2:
                prev_record=int(stack[-1])+int(stack[-2])
                stack.append(prev_record)
            elif operations[i]=="D":
                prev_record=int(stack[-1])*2
                stack.append(prev_record)
                
            elif operations[i]=="C":
                prev_record=stack.pop(-1)
                #print(prev_record)
            else:
                prev_record=operations[i]
                stack.append(prev_record)
            
        for i in stack:
            res+=int(i)
        return res


