class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substringLen = 0  # Initialize as integer
        
        for i in range(len(s)):
            substring = ""
            for j in range(i, len(s)):
                if s[j] in substring:
                    break  # Stop this substring if we hit a duplicate
                substring += s[j]
                # Update the max length found so far
                substringLen = max(substringLen, len(substring))
                
        return substringLen