# Q10. Write a program to find the smallest number using a stack.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.items=[]
        self.minimum = None
 
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)

    def getMin(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Smallest Element in given stack is : {}" .format(self.minimum))
  
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
 
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count += 1
        return self.count
 
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
 
        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
stack = Stack()
size_of_stack=int(input("Enter size of stack : "))
lst=[]
for i in range(0,size_of_stack):
    element=int(input())
    lst.append(element)
for data in lst:
    stack.push(int(data))
stack.getMin()