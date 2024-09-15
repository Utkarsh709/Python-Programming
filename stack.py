# Stack Implementation in Python
size = 4
top = -1
stack = [None] * size  

def stack_dsa():
    global top
    global stack
    while True:
        print("\nAVAILABLE CHOICES:")
        print("1 for PUSH \n2 for POP \n3 for DISPLAY \n4 to EXIT")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Enter a valid operation")

def is_full():
    return top == size - 1

def is_empty():
    return top == -1

def push():
    global top
    global stack
    if is_full():
        print("Overflow")
    else:
        push_ele = int(input("Enter a number to add on stack: "))
        top += 1
        stack[top] = push_ele
        print(f"Stack after push: {stack[:top+1]}")

def pop():
    global top
    global stack
    if is_empty():
        print("Underflow")
    else:
        pop_ele = stack[top]
        print(f"Popped element is: {pop_ele}")
        top -= 1

def display():
    global top
    global stack
    if is_empty():
        print("Stack is empty")
    else:
        print("Stack elements are:")
        for i in range(top, -1, -1):
            print(stack[i])


stack_dsa()