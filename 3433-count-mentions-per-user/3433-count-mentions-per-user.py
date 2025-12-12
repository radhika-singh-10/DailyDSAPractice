class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        n=len(events)
        res=[0]*numberOfUsers
        events.sort(key=lambda e: (int(e[1]), e[0] == "MESSAGE"))
        onlineUser=[0]*numberOfUsers
        for event in events:
            curTime=int(event[1])
            if event[0]=="MESSAGE" :
                if event[2]=="ALL":
                    for j in range(numberOfUsers):
                        res[j]+=1
                elif event[2]=="HERE":
                    for j,t in enumerate(onlineUser):
                        if t<=curTime:
                            res[j]+=1
                else:
                    for j in event[2].split():
                        res[int(j[2:])]+=1
            else:
                onlineUser[int(event[2])]=curTime+60
        return res
        

                    


                