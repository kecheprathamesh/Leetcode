# Github:   https://github.com/Kecheprathamesh
# Linkedin: https://www.linkedin.com/in/kecheprathamesh/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]