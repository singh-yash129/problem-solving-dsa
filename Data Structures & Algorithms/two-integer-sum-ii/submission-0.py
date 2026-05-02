class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in prevMap:
                # Return the stored index and current index, both +1
                return [prevMap[diff] + 1, i + 1]
            prevMap[n] = i