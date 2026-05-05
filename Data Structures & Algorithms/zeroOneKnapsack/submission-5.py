class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        row = [0]*(capacity+1)
        for prof, wei in zip(profit, weight):
            newRow = [0]*(capacity+1)
            for cap in range(capacity+1):
                if cap - wei >= 0:
                    newRow[cap] = max(row[cap], row[cap-wei]+prof)
                else:
                    newRow[cap] = row[cap]
            row = newRow
        return row[-1]
