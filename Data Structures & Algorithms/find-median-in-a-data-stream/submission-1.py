class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return
        l, r = 0, len(self.nums)
        while l != r:
            m = (r+l)//2
            if num < self.nums[m]:
                r = m-1
            elif num > self.nums[m]:
                l = m+1
            else:
                l=m=r
            self.nums.insert(l, num)
        

    def findMedian(self) -> float:
        return self.nums[len(self.nums)//2] if len(self.nums)%2 else (self.nums[len(self.nums)//2-1]+self.nums[len(self.nums)//2])/2
        