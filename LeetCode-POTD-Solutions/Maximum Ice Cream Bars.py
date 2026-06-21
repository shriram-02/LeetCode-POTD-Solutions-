class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx = max(costs)
        freq = [0] * (mx + 1)
        
        for c in costs:
            freq[c] += 1
        
        ans = 0
        
        for cost in range(1, mx + 1):
            if freq[cost] == 0:
                continue
            
            can_buy = min(freq[cost], coins // cost)
            ans += can_buy
            coins -= can_buy * cost
            
            if coins < cost:
                break
        
        return ans 	