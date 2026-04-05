class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        matrix.insert(0, [0]*(1+len(matrix[0])))
        for r in range(1, len(matrix)):
            matrix[r].insert(0, 0)
            for c in range(1, len(matrix[r])):
                matrix[r][c] += matrix[r][c-1] + matrix[r-1][c] - matrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] - self.matrix[row1][col2+1] - self.matrix[row2+1][col1] + self.matrix[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)