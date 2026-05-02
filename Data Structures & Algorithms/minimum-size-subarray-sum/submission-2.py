class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        minSubarray = float('inf')
        
        while i < len(nums):
            current_sum = 0
            j = i
            while j < len(nums):
                current_sum += nums[j]
                if current_sum >= target:
                    minSubarray = min(minSubarray, j - i + 1)
                    break
                j += 1
            i += 1
            
        return minSubarray if minSubarray != float('inf') else 0