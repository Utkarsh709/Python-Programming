size=5
queue=[None]*size
front=-1
rear=-1

def enqueue(x):
    global front
    global rear
    if (front==-1 and rear==-1):
        front=rear=0
        queue[rear]=x
    elif(((rear+1)%size)==front):
        print("overflow")
    else:
        rear=(rear+1)%size
        queue[rear]=x

def dequeue():
    global front
    global rear
    if (front==-1 and rear==-1):
        print("Underflow")
    elif (front==rear):
        front=rear=-1
    else:
        print("dequeud:",queue[front])
        front=(front+1)%size
        
def display():
    global front
    global rear
    i=front
    while(i!=rear):
        print("element is:",queue[i])
        i=(i+1)%size
    print("element is:",queue[rear])
    
def peak():
    global front 
    global rear
    if (front==-1 and rear==-1):
        print("Underflow")
    else:
        print("peak element is :",queue[front])
        

enqueue(5)
enqueue(6)
dequeue()
enqueue(7)
enqueue(8)
display()
peak()
        
