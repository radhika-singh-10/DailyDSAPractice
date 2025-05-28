class Solution:
    #count 1 [i]: the number of nodes in the first tree within distance ≤k of node i; count 2 [j]: the number of nodes in the second tree within distance ≤k−1 of node j.


    #correction in understanding after seeing the editorial
    # we can take the maximum values from the second graph and add to graph 1 asnnwer it  does not depend on specific query

    #apply bfs for each node 
    def bfs(self, adj, k, n,  start):
        visited = [False] * n
        queue = deque([(start, 0)])
        visited[start] = True
        count = 0

        while queue:
            node, dist = queue.popleft()
            if dist > k:
                continue
            count += 1
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
        return count

    def findCount(self, edges, k):
        n = max((max(u, v) for u, v in edges), default=-1) + 1
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return [self.bfs(adj, k, n, i) for i in range(n)]

    def maxTargetNodes(self, edges1, edges2, k):
        ans1 = self.findCount(edges1, k)
        ans2 = self.findCount(edges2, k - 1)
        max2 = max(ans2)
        return [a + max2 for a in ans1]
