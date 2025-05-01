class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        #topological sort- bfs - kahn's algorithm
        courseDag,inDegree=collections.defaultdict(list),[0]*(n)
        for (a,b) in relations:
            courseDag[b-1].append(a-1)
            inDegree[a-1]+=1
        # queue=collections.deque([i for i in range(n) if inDegree[i]==0])
        maxTime=[0]*n
        queue=collections.deque()
        for i in range(n):
            if inDegree[i]==0:
                queue.append(i)
                maxTime[i]=time[i]

        res=0
        while queue:
            node=queue.popleft()
            for neighbor in courseDag[node]:
                maxTime[neighbor]=max(maxTime[node]+time[neighbor],maxTime[neighbor])
                inDegree[neighbor]-=1
                if inDegree[neighbor]==0:
                    queue.append(neighbor)
                    
        return max(maxTime)


