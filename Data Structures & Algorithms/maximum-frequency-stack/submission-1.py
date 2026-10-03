class FreqStack:

    def __init__(self):
        self.stacks = []
        self.freqs = {}

    def push(self, val: int) -> None:
        if self.freqs.get(val, 0) >= len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[self.freqs.get(val, 0)].append(val)
        
        self.freqs[val] = self.freqs.get(val, 0) + 1


    def pop(self) -> int:
        val = self.stacks[-1].pop()
        not self.stacks[-1] and self.stacks.pop()
        self.freqs[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()