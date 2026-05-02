class MyHashMap:

    def __init__(self):
        self.box = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.box[key] = value

    def get(self, key: int) -> int:
        return self.box[key]

    def remove(self, key: int) -> None:
        self.box[key] = -1