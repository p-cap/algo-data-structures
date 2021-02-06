class  Stack(object):
    """
    Implementing my own stack
    reference:  

    https://digitalu.udemy.com/course/python-for-data-structures-algorithms-and-interviews/learn/lecture/3179606#overview

    """
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    # takes a look at the top item
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
s = Stack()

print (s.isEmpty())

print(s.push("Pcap"))

print (s.isEmpty())

print(s.push("is"))

print(s.push("Awesome"))

print("###### Understanding memory locations")

print(s.peek)
print(s.peek())
# <bound method Stack.peek of <__main__.Stack object at 0x0000021488894CA0>>

print(s.pop)
print(s.pop())
# <bound method Stack.pop of <__main__.Stack object at 0x0000019884B44CA0>>


print(s.peek)
print(s.peek())
# <bound method Stack.peek of <__main__.Stack object at 0x000002A8DEF44CA0>>
# After the pop, the current top of the stack takes the same memory location
# as the one that was previously popped


