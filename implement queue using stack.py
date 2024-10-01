size=5
top1=-1
top2=-1
count=0
stack1=[None]*size
stack2=[None]*size
queue=[None]*size

def push1(x):
    global top1
    if (top1==size-1):
        print("Overflow")
    else:
        top1+=1
        stack1[top1]=x
        

def push2(y):
    global top2
    if (top2==size-1):
        print("Overflow")
    else:
        top2+=1
        stack2[top2]=y   
        
        
def pop1():
    global top1
    if (top1==-1):
        print("Underflow")
    else:
        pop1_ele=stack1[top1]
        top1-=1
        return pop1_ele
        

def pop2():
    global top2
    if (top2==-1):
        print("Underflow")
    else:
        pop2_ele=stack2[top2]
        top2-=1
        return pop2_ele  
        

def enqueue(m):
    global count
    push1(m)
    count+=1
    
def dequeue():
    global count
    for i in range(0,count):
        a=pop1()
        push2(a)
    
    b=pop2() 
    count-=1
    print("Dequeud element:",b)
    
    for j in range(0,count):
        a=pop2()
        push1(a)
        

enqueue(3)
enqueue(4)
enqueue(6)
dequeue()
enqueue(1)
dequeue()
    
        
        
        
        
        
        
        
