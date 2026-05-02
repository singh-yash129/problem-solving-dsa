class MyHashSet:

    def __init__(self):
        self.box = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.box.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.box.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.box
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)