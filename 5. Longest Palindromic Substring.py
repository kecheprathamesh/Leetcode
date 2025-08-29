# Github:   https://github.com/Kecheprathamesh
# Linkedin: https://www.linkedin.com/in/kecheprathamesh/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes
            palindrome1 = expand_around_center(s, i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1

            # Even length palindromes
            palindrome2 = expand_around_center(s, i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest
