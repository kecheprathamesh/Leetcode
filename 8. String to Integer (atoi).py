# Github:   https://github.com/Kecheprathamesh
# Linkedin: https://www.linkedin.com/in/kecheprathamesh/
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = -1 if s and s[0] == '-' else 1
        if s and (s[0] == '-' or s[0] == '+'):
            s = s[1:]
                
        a = 0
        for i in s:
            if i.isdigit():
                a = a * 10 + int(i)
            else:
                break
        
        a = sign * a
        
        lower_bound = -2**31
        upper_bound = 2**31 - 1
        
        if a < lower_bound:
            return lower_bound
        elif a > upper_bound:
            return upper_bound
        else:
            return a