class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use l, r pointers for column movements
        # use t, b pointers for row movements
        # l, r = 0, len(matrix) - 1
        # while l < r:
        #     t, b = l, r
        #     for i in range(r - l):
        #         # save the topleft
        #         topLeft = matrix[t][l + i]

        #         # move bottom left into top left
        #         matrix[t][l + i] = matrix[b - i][l]

        #         # move bottom right into bottom left
        #         matrix[b - i][l] = matrix[b][r - i]

        #         # move top right into bottom right
        #         matrix[b][r - i] = matrix[t + i][r]

        #         # move top left into top right
        #         matrix[t + i][r] = topLeft
        #     l += 1
        #     r -=1

        # you can also sove this by transposing the matrix and reversing the rows
        # Transpose
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # Reverse the rows
        n = len(matrix[0])
        for r in range(len(matrix)):
            for c in range(n//2):
                matrix[r][c], matrix[r][n - c - 1] = matrix[r][n - c - 1], matrix[r][c]
