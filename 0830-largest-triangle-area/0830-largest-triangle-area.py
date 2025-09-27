class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    x1, y1 = points[i][0], points[i][1]
                    x2, y2 = points[j][0], points[j][1]
                    x3, y3 = points[k][0], points[k][1]
                    maxArea = max(maxArea, 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        return maxArea

                