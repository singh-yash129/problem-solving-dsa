class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # Stores [temperature, index]

        for i, t in enumerate(temperatures):
            # If current temp is warmer than the person in the "Waiting Room"
            while stack and t > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = i - stack_index
            
            # Current person enters the Waiting Room
            stack.append([t, i])
            
        return res