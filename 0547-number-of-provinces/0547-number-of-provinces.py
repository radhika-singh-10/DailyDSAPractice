from collections import deque,defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num=0
        n,m=len(isConnected),len(isConnected[0])
        visited=[False]*n
        graph=defaultdict(list)
        

        for i in range(n):
            if not visited[i]:
                visited[i]=True
                num+=1
                queue=deque([i])
                while queue:
                    node=queue.popleft()
                    for i in range(len(isConnected)):
                        if isConnected[node][i]==1 and not visited[i]:
                            queue.append(i)
                            visited[i]=True

        return num


