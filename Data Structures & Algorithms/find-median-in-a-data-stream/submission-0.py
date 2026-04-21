class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        return self.nums[len(self.nums)//2] if len(self.nums)%2 else (self.nums[len(self.nums)//2-1]+self.nums[len(self.nums)//2])/2
        