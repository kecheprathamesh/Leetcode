# Github:   https://github.com/Kecheprathamesh
# Linkedin: https://www.linkedin.com/in/kecheprathamesh/
class Solution:
    def reverse(self, x: int) -> int:
        
        negative = True if x<0 else False
        x=-x if negative else x
        a=0

        while x>0:
            a = (a*10)+(x%10)
            x //= 10

        if a > 2**31 - 1:
            return 0

        return a * -1 if negative else a