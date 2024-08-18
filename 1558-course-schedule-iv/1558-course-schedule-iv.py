class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = [False] * len(queries)
        if not prerequisites:
            return res
        graph = defaultdict(list)
        for i, j in prerequisites:
            graph[j].append(i)
        visited = {}
        def dfs(i, j):
            if i == j:
                return True
            if (i, j) in visited:
                return visited[(i, j)]
            for n in graph[j]:  
                if dfs(i, n):
                    visited[(i, j)] = True
                    return True
            
            visited[(i, j)] = False
            return False
        for idx, (i, j) in enumerate(queries):
            res[idx] = dfs(i, j)

        return res