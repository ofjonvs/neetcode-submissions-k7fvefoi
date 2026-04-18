class MyCalendar:
    
    def __init__(self):
        self.bookings = set()

    def book(self, startTime: int, endTime: int) -> bool:
        for booking in self.bookings:
            if booking[0] <= startTime < booking[1] or \
                booking[0] <= startTime < booking[1] or \
                startTime < booking[0] and endTime > booking[0]:
                return False
        self.bookings.add((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)