class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        # Map to store prefix sums and how many times they've occurred
        # Initialize with {0: 1} to handle cases where cur_sum == k
        prefix_sums = {0: 1}
        
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            
            # If the difference exists in our map, add its frequency to our result
            res += prefix_sums.get(diff, 0)
            
            # Update the map with the current prefix sum
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)
            
        return res