from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 1
        if 1 in count:
            ones = count[1]
            ans = ones if ones % 2 == 1 else ones - 1
        
        for x in count:
            if x == 1:
                continue
            pairs = 0
            cur = x
            while cur in count and count[cur] >= 2:
                pairs += 1
                if cur > 10**9 // cur:
                    cur = -1
                    break
                cur *= cur
            
            if pairs == 0:
                continue
            
            if cur != -1 and cur in count:
                # cur has count >= 1, use it as middle
                ans = max(ans, 2 * pairs + 1)
            else:
                # cur not present (or overflowed) -> drop one pair, use last squared value (count>=2) as middle
                ans = max(ans, 2 * (pairs - 1) + 1)
        
        return ans