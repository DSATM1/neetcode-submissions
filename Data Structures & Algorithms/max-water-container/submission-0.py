class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        
        while left < right:
            
            current_area = (right - left) * min(heights[left], heights[right])
            
            
            max_area = max(max_area, current_area)
            
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area