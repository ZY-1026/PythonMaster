from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.lru = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        self._update(key)
        return self.lru.get(key, -1)

    def put(self, key: int, value: int) -> None:
        self._update(key)
        self.lru[key] = value
        if len(self.lru) > self.capacity:
            self.lru.popitem(False)

    def _update(self, key: int) -> None:
        if key in self.lru:
            self.lru.move_to_end(key)


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.put(1, 1)
    lru.put(2, 3)
    lru.put(4, 5)
