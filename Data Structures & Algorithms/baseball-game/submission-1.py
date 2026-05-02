class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            if i == "+":
                # Sum of last two scores
                res.append(res[-1] + res[-2])
            elif i == "D":
                # Double the last score
                res.append(res[-1] * 2)
            elif i == "C":
                # Invalidate/Remove the last score
                res.pop()
            else:
                # If it's not a special char, it's a number (positive or negative)
                res.append(int(i))
                
        return sum(res)