class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

top = None

def push(x):
    global top
    newnode = Node(x)
    newnode.next = top  
    top = newnode  

def pop():
    global top
    if top is None:  
        print("Stack is empty")
        return
    pop_ele = top.data  
    top = top.next  
    print("Popped element:", pop_ele)

def display():
    global top
    if top is None:  
        print("Stack is empty")
        return
    temp = top
    while temp is not None:  
        print("Value:", temp.data)
        temp = temp.next

push(2)
push(3)
push(4)
push(5)
pop()
display()
