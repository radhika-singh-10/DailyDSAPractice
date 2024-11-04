class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        else:
            counter,interval=Counter(tasks),set()
            counter=sorted(counter.values(),reverse=True)
            max_freq=max(counter)
            return max((max_freq-1)*(n+1)+counter.count(max_freq),len(tasks))
            