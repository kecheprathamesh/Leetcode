# Github:   https://github.com/Kecheprathamesh
# Linkedin: https://www.linkedin.com/in/kecheprathamesh/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        direction=False
        a=[""]*numRows
        curr=0
        for char in s:
            a[curr]+=char
            if curr==0 or curr==numRows-1:
                direction=not direction
            curr+=1 if direction else -1
        return "".join(a)