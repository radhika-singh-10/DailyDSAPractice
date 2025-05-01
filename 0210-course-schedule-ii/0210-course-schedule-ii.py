from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #edge cases and approach
        #prerequesites->[a,b], b->a
        #noof courses>prereq??
        #no prereq-> no of courses->loop to ans (0-n-1)->ans
        #graph method
        #{0->[],1->[0],2->[0],3->[1,2]}
        #if circle-> {0->[3],1->[0],2->[0],3->[1,2]}->empty ans
        #visited=set() ->bfs
        #topological sort - bfs - kahn's algorithm
        
        graph = defaultdict(list)
        in_degree=[0]*numCourses
        #here it is confusing to creeate a dag
        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1
        queue=deque([i for i in range(numCourses) if in_degree[i]==0])
        res=[]
        while queue:
            node=queue.popleft()
            res.append(node)
            for neigbour in graph[node]:
                in_degree[neigbour]-=1
                if in_degree[neigbour]==0:
                    queue.append(neigbour)

        return res if len(res)==numCourses else []

