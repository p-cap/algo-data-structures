class PcapDeque(object):

    def __init__(self):
        self.items = []
    
    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()
        # or return self.items.pop(0)
    
    def removeRear(self):
        self.items.reverse()
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def showDeque(self):
        return self.items

p = PcapDeque()

print(p.size())
print(p.isEmpty())


print("### Adding the Front")
p.addFront("Pcap")
print(p.showDeque())
p.addFront("is")
print(p.showDeque())
p.addFront("Awesome")
print(p.showDeque())

print("### Adding to the rear")
p.addRear("Great")
print(p.showDeque())
p.addRear("The")
print(p.showDeque())

print("### Removing items from the front")
print(p.removeFront())
print(p.showDeque())

print("### Removing items from the Rear")
print(p.removeRear())
print(p.showDeque())


