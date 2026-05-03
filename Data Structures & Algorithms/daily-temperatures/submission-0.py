class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(temperatures):
            j = i + 1
            found_warmer = False # Track if we found a higher temp
            
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    found_warmer = True
                    break
                j += 1
            
            # If the inner loop finished and found nothing, append 0
            if not found_warmer:
                res.append(0)
                
            i += 1
        return res