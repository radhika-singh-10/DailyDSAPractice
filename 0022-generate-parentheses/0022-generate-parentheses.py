class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        elif n==1:
            return ["()"]
        def backtrack(cur_str,l,r):
            if len(cur_str)==2*n:
                res.append("".join(cur_str))
                return 
            if l<n:
                cur_str.append("(")
                backtrack(cur_str,l+1,r)
                cur_str.pop()
            if l>r:
                cur_str.append(")")
                backtrack(cur_str,l,r+1)
                cur_str.pop()
        res=[]
        backtrack([],0,0)
        return res


        