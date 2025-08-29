# Github:   https://github.com/Kecheprathamesh
# Linkedin: https://www.linkedin.com/in/kecheprathamesh/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = set()
        l = 0
        j = 0
        for i in s:
            if i in k:
                l = max(len(k), l)
                while i in k:
                    k.remove(s[j])
                    j += 1
                k.add(i)
            else:
                k.add(i)
                l = max(len(k), l)
        return l