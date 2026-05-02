class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n 
        for _ in range(k):
            # Pop from the end, insert at the beginning
            nums.insert(0, nums.pop())