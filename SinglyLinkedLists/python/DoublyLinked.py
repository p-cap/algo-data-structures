class PcapDoublyLinkedList(object):

    def __init__(self):
        self.head = None

class PcapNode():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# decalred the list
pcapList = PcapDoublyLinkedList()

# declared the nodes
pcapHead = PcapNode("Uno")
pcapNode2 = PcapNode("Dos")
pcapNode3 = PcapNode("Tres")

# assign head to the list class
pcapList.head = pcapHead

# link all 3 modes together
pcapHead.next = pcapNode2
pcapHead.previous = None

pcapNode2.next = pcapNode3
pcapNode2.previous = pcapHead

pcapNode3.next = None
pcapNode3.previous = pcapNode2

print(pcapHead.value)
print(pcapHead.next.value)
print(pcapHead.next.next.value)

print("#######################################")

print(pcapNode3.value)
print(pcapNode3.previous.value)
print(pcapNode3.previous.previous.value)



