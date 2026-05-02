class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        current_sum = 0
        # Initialize with a value larger than any possible subarray
        min_len = float('inf') 
        
        for r in range(len(nums)):
            current_sum += nums[r]
            
            # While the consecutive subarray sum is enough
            while current_sum >= target:
                # Update our minimum length
                min_len = min(min_len, r - l + 1)
                
                # Shrink the window from the left to find a smaller one
                current_sum -= nums[l]
                l += 1
                
        # If min_len was never updated, return 0 per instructions
        return min_len if min_len != float('inf') else 0