class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, element):
        self.q.append(element)

    def dequeue(self):
        return self.q.pop(0)

    def access(self):
        return self.q[0]

    def isempty(self):
        return not len(self.q)

    def size(self):
        return len(self)


qq = Queue()
qq.enqueue("first")
qq.enqueue("second")
print(qq.access())
print(qq.dequeue())
print(qq.access())
