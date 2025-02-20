class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #"bcabc"->"abc", "cbacdcbc"-> "acdb"
        stack,visited=[],set()
        last_occurence={c: i for i, c in enumerate(s)}#Counter(s)
        # print(freq,Counter(s))
        # for i,c in enumerate(s):
        #     print(i,c)
        for i,c in enumerate(s):
            if c not in visited:
                while stack and stack[-1]>c and i<last_occurence[stack[-1]]:
                    visited.discard(stack.pop())
                visited.add(c)
                stack.append(c)
        return ''.join(stack)
                
        
        # freq=Counter(s)
        # pos=0
        # for i in range(len(s)):
        #     if s[i]<s[pos]:
        #         pos=i
        #     freq[s[i]]-=1
        #     if freq[s[i]]==0:
        #         break

        # return s[pos]+ self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''

