from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #n rooms - 0-n-1
        res=False
        #visited=[0]*n
        #apply bfs
        #make a graph, key-room if, value-keys
        #till all the room are visited, and all the rooms are locked- return True else False
        #queue=room id, 

        n=len(rooms)
        queue=deque([0])
        visited=[False]*n
        

        while queue:
            cur_room=queue.popleft()
            visited[cur_room]=True
            for i in rooms[cur_room]:
                if not visited[i]:
                    queue.append(i)

        
        return all(visited)
