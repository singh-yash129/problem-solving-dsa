class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def two_sum(start_idx, current_target, quadruplet_prefix):
            left, right = start_idx, len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == current_target:
                    res.append(quadruplet_prefix + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif current_sum < current_target:
                    left += 1
                else:
                    right -= 1

        # First level loop (Fixing the 1st number)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Second level loop (Fixing the 2nd number)
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Now we look for two numbers that sum up to:
                # new_target = target - (nums[i] + nums[j])
                new_target = target - nums[i] - nums[j]
                two_sum(j + 1, new_target, [nums[i], nums[j]])
        
        return res