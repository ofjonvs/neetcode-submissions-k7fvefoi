class MyCalendar:
    
    def __init__(self):
        self.bookings = Tree()

    def book(self, startTime: int, endTime: int) -> bool:
        return self.bookings.insert((startTime, endTime))

class Node:
    def __init__(self, booking):
        self.booking = booking
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, booking):
        if self.root is None:
            self.root = Node(booking)
            return True
        cur = self.root
        parent = None
        while cur is not None:
            parent = cur
            if booking[1] <= cur.booking[0]:
                cur = cur.left
            elif booking[0] >= cur.booking[1]:
                cur = cur.right
            else:
                return False
        if booking[1] <= parent.booking[0]:
            parent.left = Node(booking)
        else:
            parent.right = Node(booking)
        return True
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)