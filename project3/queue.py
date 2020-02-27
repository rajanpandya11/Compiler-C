class Queue(object):

    def __init__(self):
        self.items = []
        self.i = len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
        self.i += 1

    def dequeue(self):
        self.i -= 1
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printq(self):
        print self.items

    def qfront(self):
        return self.items[len(self.items)-1]

    def currenttoken(self):
        if 0 < self.i <= len(self.items):
            return self.items[self.i-1]

    def accept(self):
        self.i -= 1

    def indexed(self, n):
        if 0 < n <= len(self.items):
            return self.items[n-1]