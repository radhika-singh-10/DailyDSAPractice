class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sort - dag using bfs - kahn's algorithm
        if not prerequisites:
            return True
        pr={}
        in_degree = [0] * numCourses
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in pr:     
                pr[prerequisites[i][0]]=[]
            pr[prerequisites[i][0]].append(prerequisites[i][1])
            in_degree[prerequisites[i][1]] += 1

        queue=deque([i for i in range(numCourses) if in_degree[i]==0])
        # for i in range(numCourses):
        #     if in_degree[i] == 0:
        #         queue.append(i)


        while queue:
            c = queue.popleft()
            if c in pr:
                for p in pr[c]:
                    in_degree[p] -= 1
                    if in_degree[p] == 0:
                        queue.append(p)


        return all(deg == 0 for deg in in_degree)
