class CountSquares:

    def __init__(self):
        from collections import defaultdict
        self.xMap = defaultdict(lambda: defaultdict(int))
        self.yMap = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.xMap[point[0]][point[1]] += 1
        self.yMap[point[1]][point[0]] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for y in self.xMap[px]:
            if y != py:
                dist = abs(y - py)
                x_left = px - dist
                res += self.xMap[px][y] * self.xMap[x_left][py] * self.xMap[x_left][y]
                
                x_right = px + dist
                res += self.xMap[px][y] * self.xMap[x_right][py] * self.xMap[x_right][y]

        return res