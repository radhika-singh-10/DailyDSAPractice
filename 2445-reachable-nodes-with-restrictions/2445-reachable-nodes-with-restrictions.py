from collections import deque, defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res,queue=0,deque([0])
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        visited=[False]*n
        visited[0]=True
        queue.append(0)
        for node in restricted:
            visited[node] = True

        while queue:
            cur=queue.popleft()
            #if cur not in restricted:
            #res+=1
            for node in graph[cur]:
                if not visited[node]:
                    visited[node]=True
                    queue.append(node)
        return sum(visited)-len(restricted)


        