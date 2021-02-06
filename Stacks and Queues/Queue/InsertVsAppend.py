class Pcap(object):

    def __init__(self):
        self.items = []

    def myInsert(self,items):
        self.items.insert(0, items)

    def mySize(self):
        return len(self.items)

    def myAppend(self, items):
        self.items.append(items)
    
    def myDequeue(self):
        return self.items.pop()

    def showMe(self):
        return self.items


p = Pcap()

print(p.mySize())

# print(p.myInsert("Pcap"))
# print(p.myInsert("is"))
# print(p.myInsert("Awesome"))

print(p.myAppend("Pcap"))
print(p.myAppend("is"))
print(p.myAppend("Awesome"))

print(p.mySize())
print(p.showMe())

print(p.myDequeue())
print(p.mySize())
