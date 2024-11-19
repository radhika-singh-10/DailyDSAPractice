class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="" or len(digits)==0:
            return []
        phone_dict={"0":"","1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        
        # for digit in range(len(digits)):
        #     digit_alpha=phone_dict[int(digit)]
        #     for i in digit_alpha:


        def backtrack(i,path):
            if len(path)==len(digits):
                res.append("".join(path))
                return 

            letters = phone_dict[digits[i]]
            for letter in letters:
                path.append(letter)
                backtrack(i+1,path)
                path.pop()

           
        backtrack(0,[]) 
        return res   

        