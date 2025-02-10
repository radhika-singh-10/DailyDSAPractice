class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        mp = defaultdict(list)
        for n in groups:
            if n in mp: continue
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    mp[n].append(i)
                    if n // i != i:
                        mp[n].append(n // i)


        hashmap = defaultdict(int)
        for i, val in enumerate(elements):
            if val not in hashmap:
                hashmap[val] = i

        res = [-1] * len(groups)
        for i, num in enumerate(groups):
            divs = mp[num]
            idx = len(elements)
            for d in divs:
                if d in hashmap:
                    idx = min(idx, hashmap[d])


            idx = -1 if idx == len(elements) else idx
            res[i] = idx

        return res
            