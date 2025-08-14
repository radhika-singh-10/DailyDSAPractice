class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        
        total=Counter(basket1) + Counter(basket2)
        for count in total.values():
            if count % 2 != 0:
                return -1
        fruits_to_swap,c1 = [], Counter(basket1)
        for fruit, total_count in total.items():
            target = total_count // 2
            diff = c1.get(fruit, 0) - target
            for _ in range(abs(diff)):
                fruits_to_swap.append(fruit)

        fruits_to_swap.sort()
        min_val,total_cost = min(total.keys()), 0
        swaps_to_make = len(fruits_to_swap) // 2
        for i in range(swaps_to_make):
            total_cost += min(fruits_to_swap[i], 2 * min_val)
            
        return total_cost
