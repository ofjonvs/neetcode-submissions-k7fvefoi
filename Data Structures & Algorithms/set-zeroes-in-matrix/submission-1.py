class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            for col in range(1, len(matrix[0])):
                row[col] = 'x' if row[col-1] in (0, 'x') and row[col] else row[col]
            for col in range(len(matrix[0])-2, -1, -1):
                row[col] = 'x' if row[col+1] in (0, 'x') and row[col] else row[col]
        
        for col in range(len(matrix[0])):
            for row in range(1, len(matrix)):
                matrix[row][col] = 0 if matrix[row-1][col] == 0 else matrix[row][col]
            for row in range(len(matrix)-2, -1, -1):
                matrix[row][col] = 0 if matrix[row+1][col] == 0 else matrix[row][col]
        
        for row in matrix:
            for col, val in enumerate(row):
                row[col] = 0 if val == 'x' else val 
        