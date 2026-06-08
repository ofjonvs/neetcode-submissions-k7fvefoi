class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        for layer in range((min(len(matrix), len(matrix[0]))+1)//2):
            colStart, colEnd = layer, len(matrix[0])-layer-1
            
            for c in range(colStart, colEnd):
                res.append(matrix[layer][c])

            for r in range(layer, len(matrix)-layer-1):
                res.append(matrix[r][colEnd])

            for c in range(colEnd, colStart, -1):
                res.append(matrix[-layer-1][c])

            for r in range(len(matrix)-layer-1, layer, -1):
                res.append(matrix[r][colStart])

        if len(res) != len(matrix)*len(matrix[0]):
            res.append(matrix[len(matrix)//2][len(matrix[0])//2])
        return res[:len(matrix)*len(matrix[0])]
            