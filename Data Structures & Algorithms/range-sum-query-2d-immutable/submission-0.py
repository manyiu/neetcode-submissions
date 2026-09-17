class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                top = matrix[i - 1][j] if i > 0 else 0
                left = matrix[i][j - 1] if j > 0 else 0
                top_left = matrix[i - 1][j - 1] if i > 0 and j > 0 else 0
                matrix[i][j] = top + left - top_left + cell

        self.prefix_sum = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.prefix_sum[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix_sum[row2][col1 - 1] if col1 > 0 else 0
        top_left = self.prefix_sum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        total = self.prefix_sum[row2][col2] - top - left + top_left

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)