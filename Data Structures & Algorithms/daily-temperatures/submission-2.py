class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. Create a list of zeros the same length as the input
        res = [0] * len(temperatures) 
        
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    # 2. Update the specific spot if we find a warmer day
                    res[i] = j - i
                    break
        return res