class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: a list of zero or one elements is already sorted
        if len(nums) <= 1:
            return nums

        # 1. Divide: Find the midpoint and split the array
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        # 2. Conquer: Merge the two sorted halves
        return self.merge(left_half, right_half)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_arr = []
        i = j = 0

        # Compare elements from both halves and append the smaller one
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        # Append any remaining elements (one of these will be empty)
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        
        return sorted_arr