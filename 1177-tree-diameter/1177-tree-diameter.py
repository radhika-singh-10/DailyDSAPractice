from collections import defaultdict, deque

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # def dfs(i,visited):
        #     nonlocal diameter
        #     visited.add(i)
        #     distance,distance_one,distance_two=0,0,0
        #     for neighbour in graph:
        #         if neighbour not in visited:
        #             distance=1+dfs(neighbour,visited)
        #         if distance>distance_two:
        #             distance_one,distance_two=distance,distance_one
        #         elif distance>distance_one+distance_two:
        #             distance_two=distance
        #     diameter=max(diameter,distance_one+distance_two)

        #     return distance_one

        def bfs(start):
            visited = set()
            queue = deque([(start, 0)])  # (node, distance)
            visited.add(start)
            farthest_node = start
            max_distance = 0

            while queue:
                node, distance = queue.popleft()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append((neighbour, distance + 1))
                        visited.add(neighbour)
                        if distance + 1 > max_distance:
                            max_distance = distance + 1
                            farthest_node = neighbour
            return farthest_node, max_distance

        if not edges:
            return 0

        # Create adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # First BFS to find the farthest node from an arbitrary node (e.g., node 0)
        arbitrary_node = 0
        farthest_node, _ = bfs(arbitrary_node)

        # Second BFS from the farthest node found in the first BFS
        _, diameter = bfs(farthest_node)

        return diameter




        