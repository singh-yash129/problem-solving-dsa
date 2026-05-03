class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        
        # Shrink the window until it is size k
        while r - l + 1 > k:
            # Compare distances of the elements at the boundaries
            if abs(arr[l] - x) <= abs(arr[r] - x):
                # The left side is closer or equal, so remove the right side
                r -= 1
            else:
                # The right side is closer, so remove the left side
                l += 1
                
        return arr[l : r + 1]