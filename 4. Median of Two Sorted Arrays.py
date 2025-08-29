# Github:   https://github.com/Kecheprathamesh
# Linkedin: https://www.linkedin.com/in/kecheprathamesh/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res.sort()
        n=len(res)
        if n%2==0:
            ans=(res[n//2 -1]+res[n//2 ] )/2
        else:
            ans= res[n//2 ]
        return float(ans)
        