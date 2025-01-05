class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # edge case-> 1 word-> no reverse,
        # special character allowed- space ' '
        # approach - reverse whole string then reverse the each word
        #reverse the string
        #for each word we reverse the string 

        def reverse(i, j, s):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        n = len(s)
        reverse(0, n - 1, s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] != ' ':
                j += 1
            reverse(i, j - 1, s)
            i = j + 1  





                
        
        
#         new_str= "".join(s)
#         s.append("-")
#         word=""
#         print(s)
#         for i in new_str:
#             if i == " ":
#                 s.append(" ")  
#             s.append(i) 
            
#         print(s)
#         # for i in s:
#         #     if i=="-":
#         #         s.remove("-")
#         #         break
#         #     s.remove(i)
#         #     print(s)
            
#         while "-" in s:
#             s.pop(0)
            
# #             s.append(" ")
# #             print(s)


#         # while len(s) > len(new_str):  
#         #     s.pop(0)

        
            
        