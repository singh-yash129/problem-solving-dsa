class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # While the number is in the valid range (1 to n) 
            # and not in its correct position (nums[i] - 1)
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap it to its target index
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]
        
        # Second pass to find the first index that doesn't match
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all numbers 1..n are present
        return n + 1