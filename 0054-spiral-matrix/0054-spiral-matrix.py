class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowBegin, rowEnd = 0, len(matrix) - 1
        colBegin, colEnd = 0, len(matrix[0]) - 1
        spiral = []
        if len(matrix) == 0:
            return spiral

        while rowBegin <= rowEnd and colBegin <= colEnd:
            # right traversal
            for i in range(colBegin, colEnd + 1):
                spiral.append(matrix[rowBegin][i])
            rowBegin += 1

            # down
            for i in range(rowBegin, rowEnd + 1):
                spiral.append(matrix[i][colEnd])
            colEnd -= 1

            # left
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    spiral.append(matrix[rowEnd][i])
                rowEnd -= 1

            # up
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    spiral.append(matrix[i][colBegin])
                colBegin += 1
        return spiral
