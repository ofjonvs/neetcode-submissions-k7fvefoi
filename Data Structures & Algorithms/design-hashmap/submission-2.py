class MyHashMap:

    def __init__(self):
        self.n = 1000
        self.hashMap = [[] for _ in range(self.n)]

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hashMap[key%self.n])):
            if self.hashMap[key%self.n][i][0] == key:
                self.hashMap[key%self.n][i] = (key, value)
                return
        self.hashMap[key%self.n].append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.hashMap[key%self.n]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashMap[key%self.n])):
            if self.hashMap[key%self.n][i][0] == key:
                self.hashMap[key%self.n].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)