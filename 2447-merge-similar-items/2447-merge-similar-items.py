class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hm={}
        for i in range(len(items1)):
            if items1[i][0] in hm:
                hm[items1[i][0]]+=items1[i][1]
            else:
                hm[items1[i][0]]=items1[i][1]

        for i in range(len(items2)):
            if items2[i][0] in hm:
                hm[items2[i][0]]+=items2[i][1]
            else:
                hm[items2[i][0]]=items2[i][1]

        res=[[key, value] for key, value in hm.items()]
        res.sort(key=lambda x: x[0])
        return res

