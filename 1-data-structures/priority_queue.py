import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


def main():
    q = PriorityQueue()
    q.push(Item("Thales 0"), 1)
    q.push(Item("Thales 1"), 5)
    q.push(Item("Thales 2"), 4)
    q.push(Item("Thales 3"), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

if __name__ == "__main__":
    main()