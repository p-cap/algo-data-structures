class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def cycle_checker(self):
        marker1 = self
        marker2 = self

        while marker2 != None and marker2.next != None:

            marker1 = marker1.next
            marker2 = marker2.next.next

            print("#######")
            print(marker1.value)
            print(marker2.value)

            if marker1 == marker2: 
                return True

        return False

###### Test Case # 1 ######
print("###### Test Case # 1 ######")
print('\n')
print("###### True ######")
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
# this points back to the head of the singly linked list
c.next = a

print('\n')
print("Cyclic Check for a: " + str(a.cycle_checker()))

print('\n')

###### Test Case # 1 ######
print("###### Test Case # 2 ######")
print('\n')
print("###### False ######")
# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z

print('\n')
print("Cyclic Check for a: " + str(x.cycle_checker()))