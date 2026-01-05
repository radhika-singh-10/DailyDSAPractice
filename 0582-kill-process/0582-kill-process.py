from collections import deque
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        #create a dag
        dag = collections.defaultdict(list)
        for i in range(len(ppid)):
            dag[ppid[i]].append(pid[i])

        queue = collections.deque()
        queue.append(kill)
        result = []
        while queue:
            killed = queue.popleft()
            result.append(killed)
            if killed in dag:
                queue.extend(dag[killed])

        return result

        

