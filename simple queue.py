size=5
queue=[None]*size
front=-1
rear=-1

def enqueue(x):
    global front
    global rear
    if (rear==size-1):
        print("Overflow")
    elif (front==-1 and rear==-1):
        front=rear=0
        queue[rear]=x
    else:
        rear+=1
        queue[rear]=x
        
def dequeue():
    global front
    global rear
    if (front==-1 and rear==-1):
        print("Underflow")
    elif (front == rear):
        front=rear=-1
    else:
        print("dequed element:",queue[front])
        front+=1
        
def display():
    global front
    global rear
    if (front==-1 and rear==-1):
        print("Underflow")
    else:
        for i in range(front,rear+1):
            print(i,"element is:",queue[i])
            
def peak():
    global front
    global rear
    if (front==-1 and rear==-1):
        print("Underflow")
    else:
        print("top element is:",queue[front])
        
enqueue(4)
enqueue(6)
dequeue()
enqueue(8)
peak()
display()
    
            
    