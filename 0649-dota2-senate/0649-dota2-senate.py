from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #senator can execerice either of 2 below rules
        #1 senator can make other senator lose all his rights in this and following rounds
        #2 senator found senators from his team have still right to vote, they can decide on the change in the game
        #senators with no voting rights will be skipped- continue
        #senator - R/D, each has voting right
        n,r_queue,d_queue=len(senate),deque(),deque()
        for i, s in enumerate(senate):
            if s=='R':
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            r_turn,d_turn=r_queue.popleft(),d_queue.popleft()
            if r_turn<d_turn:
                r_queue.append(r_turn+n)
            else:
                d_queue.append(d_turn+n)

        return "Radiant" if r_queue else "Dire"