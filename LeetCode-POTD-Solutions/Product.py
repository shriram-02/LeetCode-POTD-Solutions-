class Solution:
    def isProduct(self, arr, target):
        seen = set()
        
        for x in arr:
            
            if x == 0:
                if target == 0 and seen:
                    return True
            else:
                if target % x == 0 and (target // x) in seen:
                    return True
            
            seen.add(x)
        
        return False