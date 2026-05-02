class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        while m <= (m+n) and i <= n-1:
            nums1[m]=nums2[i]
            m+=1
            i+=1

        nums1.sort()    