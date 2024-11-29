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
        #topological sort - bfs
        
        
        graph = defaultdict(list)
        for course,prereq in prerequisites:
            graph[prereq].append(course)
        in_degree=[0]*numCourses
        for course,prereq in prerequisites:
            in_degree[course]+=1
        queue=deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        res=[]
        while queue:
            node=queue.popleft()
            res.append(node)
            for neigbour in graph[node]:
                in_degree[neigbour]-=1
                if in_degree[neigbour]==0:
                    queue.append(neigbour)


        if len(res)<numCourses:
            return []

        return res
