class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number=set(nums)
        longest=0
        for n in nums:
            if n-1 not in number:
                length=0
                while (n+length) in number:
                    length+=1
                longest=max(longest,length)
        return longest
                
