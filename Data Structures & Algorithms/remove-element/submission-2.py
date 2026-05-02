class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 'k' acts as the pointer for the next position of a non-val element
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                # Move the valid element to the front
                nums[k] = nums[i]
                k += 1
        
        # k is the count of elements not equal to val
        return k