class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]
        #edges = sorted(edges, key=lambda x: x[0])
        for edge in edges:
            graph[edge[0]].append(edge[1])
        print(graph)
        #topological sort using dfs - easier than bfs(kanh's algo)
        
        for i in range(n):
            visited=[False]*n
            self.dfs(graph,i,i,res,visited)
        for i in range(n):
            res[i].sort()
        return res
    
    def dfs(self, graph, parent, cur,res, visited):
        visited[cur]=True
        for child in graph[cur]:
            if not visited[child]:
                res[child].append(parent)
                self.dfs(graph,parent,child,res,visited)
    







