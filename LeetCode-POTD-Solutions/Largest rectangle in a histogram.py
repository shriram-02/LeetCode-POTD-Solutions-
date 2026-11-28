class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            curr = heights[i] if i < len(heights) else 0

            while stack and heights[stack[-1]] > curr:
                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area