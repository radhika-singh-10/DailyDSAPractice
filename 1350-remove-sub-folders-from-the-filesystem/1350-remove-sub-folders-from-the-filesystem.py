class Solution:
    # class TrieNode:
    #     def __init__(self):
    #         self.letter=[0]*26
    #         self.folderEnd=False
    
    # def __init__(self):
    #     self.root=TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        #union find 
        #n.l.logn [l-letter compariosns] - tc
        #n - sc
        folder.sort()
        res=[folder[0]]
        
        for i in range(1,len(folder)):
            prev=res[-1]
            prev+="/"
            if not folder[i].startswith(prev):
                res.append(folder[i])
        return res
                


                


