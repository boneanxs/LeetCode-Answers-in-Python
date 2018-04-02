class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxV = 0
        lower = 0
        length = len(height)
        higher = length - 1
        while lower < higher:
            maxV = max(maxV,(higher - lower) * min(height[lower],height[higher]))
            if height[lower] < height[higher]:
                lower +=1
            else:
                higher -=1
        return maxV