class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s, i = set(nums), 1
        while i in s: i += 1
        return i