class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxA = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                A = (j - i) * min(heights[i], heights[j])
                maxA = max(maxA, A)
        return maxA

        