class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res=0

        domino_map=collections.defaultdict(int)
        for x,y in dominoes:
            val=x*10+y if x<=y else y*10+x 
            res+=domino_map[val]
            domino_map[val]+=1
        return res
            
        # for i in range(len(dominoes)):
        #     if (dominoes[i][0],dominoes[i][1]) not in domino_map:
                
        #         domino_map.add((dominoes[i][0],dominoes[i][1]))
        #         domino_map.add((dominoes[i][1],dominoes[i][0]))
                
        #         print(i,dominoes[i],(dominoes[i][0],dominoes[i][1]),domino_map)
        #     else:
        #         #if (dominoes[i][1],dominoes[i][0]) in domino_map:
        #         res+=1

            
        #     #print(domino_map,res,dominoes[i])

        # return res


