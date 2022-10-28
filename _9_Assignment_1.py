# Q9. Write a program to reverse a stack.
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
    def display(self):
        for data in reversed(self.items):
            print(data)
 
def insert_at_bottom(s, data):
    if s.is_empty():
        s.push(data)
    else:
        popped = s.pop()
        insert_at_bottom(s, data)
        s.push(popped)
 
def reverse_stack(s):
    if not s.is_empty():
        popped = s.pop()
        reverse_stack(s)
        insert_at_bottom(s, popped)
 
s = Stack()
size_of_stack=int(input("Enter size of stack : "))
lst=[]
for i in range(0,size_of_stack):
        element=int(input())
        lst.append(element)
for data in lst:
    s.push(int(data))

print('Original stack : ')
s.display()
reverse_stack(s)
print('Stack after reversing : ')
s.display()