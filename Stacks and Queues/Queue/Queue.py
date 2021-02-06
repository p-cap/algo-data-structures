class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.insert(0, item)  

    def dequeue(self):
        return self.items.pop()      

    def showQueue(self):
        for i in self.items:
            return i

q = Queue()

print(q.isEmpty())
print(q.size())

q.enqueue("Pcap")
q.enqueue("is")
q.enqueue("Awesome")

print(q.showQueue())

print(q.isEmpty())
print(q.size())
print(q.dequeue)
print(q.dequeue())
