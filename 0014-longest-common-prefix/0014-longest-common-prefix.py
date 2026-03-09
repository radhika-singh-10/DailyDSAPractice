class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        def lcp(leftStr,rightStr):
            minLen=min(len(leftStr),len(rightStr))
            for i in range(minLen):
                if leftStr[i]!=rightStr[i]:
                    return leftStr[:i]
            return leftStr[:minLen]

        def divideAndConquer(strs,l,r):
            if l==r:
                return strs[l]
            else:
                m=(l+r)//2
                lcpLeft=divideAndConquer(strs,l,m)
                lcpRight=divideAndConquer(strs,m+1,r)
                return lcp(lcpLeft,lcpRight)
        return divideAndConquer(strs,0,len(strs)-1)
        # n=len(strs)
        # if n==0:
        #     return ""
        # prefix=strs[0]
        # for i in range(1,n):
        #     while strs[i].find(prefix)!=0:
        #         prefix=prefix[0:len(prefix)-1]
        #         if prefix=="":
        #             return ""

        # return prefix
        
