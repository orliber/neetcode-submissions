class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = min(heights[l], heights[r]) * (r - l)
        while l < r:
            tmp = min(heights[l], heights[r]) * (r - l)
            if area < tmp:
                area = tmp
            elif heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return area
            