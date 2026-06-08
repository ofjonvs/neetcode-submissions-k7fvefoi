class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for layer in range(len(matrix) // 2):
            for col in range(layer, len(matrix)-layer-1):
                r1, c1 = layer, col
                tmp = matrix[r1][c1]
                for r2, c2 in ((col, -layer-1), (-layer-1, -col-1), (-col-1, layer), (layer, col)):
                    matrix[r2][c2], tmp =  tmp, matrix[r2][c2]
