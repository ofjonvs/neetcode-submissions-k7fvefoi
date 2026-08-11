class MyHashMap:

    def __init__(self):
        self.hashMap = [[] for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hashMap[key%10000])):
            if self.hashMap[key%10000][i][0] == key:
                self.hashMap[key%10000][i] = (key, value)
                return
        self.hashMap[key%10000].append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.hashMap[key%10000]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashMap[key%10000])):
            if self.hashMap[key%10000][i][0] == key:
                self.hashMap[key%10000].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)