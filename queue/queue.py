class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def __repr__(self):
        return f"{self.storage}"

    def enqueue(self, item):
        self.size += 1
        return self.storage.insert(0, item)

    def dequeue(self):
        if self.len() < 1:
            return None
        self.size -= 1
        return self.storage.pop()

    def len(self):
        return self.size


q = Queue()

q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
print(q)
