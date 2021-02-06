class PcapSinglyLinkedList():
    def __init__(self):
        self.head = None


class PcapNode():
    def __init__(self, value):
        self.value = value
        self.nextNode = None

pcapList = PcapSinglyLinkedList()

# Created the head of the linked list
pcapList.head = PcapNode("Lunes")

# assigning each node variable
day1 = pcapList.head
day2 = PcapNode("Martes")
day3 = PcapNode("Miyerkules")
day4 = PcapNode("Huwebes")
day5 = PcapNode("Biyernes")
day6 = PcapNode("Sabado")
day7 = PcapNode("Linggo")

print(day1.value)
print(day2.value)
print(day3.value)
print(day4.value)
print(day5.value)
print(day6.value)
print(day7.value)

print("#######################################")

# We can now link them together
day1.nextNode = day2
day2.nextNode = day3
day3.nextNode = day4
day4.nextNode = day5 
day5.nextNode = day6
day6.nextNode = day7
day7.nextNode = None

days = [day1, day2, day3, day4, day5, day6, day7]

for i in days:
    print(i.value)