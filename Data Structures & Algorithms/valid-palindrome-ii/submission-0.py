class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                # If we find a mismatch, try deleting s[i] OR s[j]
                # Check the two remaining substrings
                return is_palindrome(i + 1, j) or is_palindrome(i, j - 1)
            i += 1
            j -= 1
            
        return True