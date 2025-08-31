# Github:   https://github.com/Kecheprathamesh
# Linkedin: https://www.linkedin.com/in/kecheprathamesh/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        right=len(height)-1
        left=0
        area=0
        while right>left:
            area=max(area,min(height[left],height[right])*(right-left))
        
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
                
        return area 