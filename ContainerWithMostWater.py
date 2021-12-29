class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        max_left = 0
        max_right = len(height) - 1
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            if current_area > max_area:
                max_left = left
                max_right = right
                max_area = current_area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
