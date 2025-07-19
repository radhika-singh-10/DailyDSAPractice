class Solution:
    class TrieNode:
        def __init__(self):
            self.children={}#[0]*26
            self.folderEnd=False
    
    def __init__(self):
        self.root=self.TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        #union find 
        for path in folder:
            cur_node=self.root
            folders=path.split("/")

            for name in folders:
                if name=="":
                    continue
                if name not in cur_node.children:
                    cur_node.children[name]=self.TrieNode()
                cur_node=cur_node.children[name]
            cur_node.folderEnd=True

        res=[]
        for path in folder:
            cur_node=self.root
            folders=path.split("/")
            isSubFolder=False
            for i,folderName in enumerate(folders):
                if folderName=="":
                    continue
                nextNode=cur_node.children[folderName]
                if nextNode.folderEnd and i!=len(folders)-1:
                    isSubFolder=True
                    break
                cur_node=nextNode
            if not isSubFolder:
                res.append(path)
        return res








        #n.l.logn [l-letter compariosns] - tc
        #n.l - sc
        # folder.sort()
        # res=[folder[0]]
        
        # for i in range(1,len(folder)):
        #     prev=res[-1]
        #     prev+="/"
        #     if not folder[i].startswith(prev):
        #         res.append(folder[i])
        # return res
                


                


