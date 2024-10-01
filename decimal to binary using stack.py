top = -1
size = 10
stack = [None] * size

def push(x):
    global top
    if top == size - 1:
        print("Overflow")
    else:
        top += 1
        stack[top] = x

def pop():
    global top
    if top == -1:
        print("Underflow")
        return None
    else:
        pop_ele = stack[top]
        top -= 1
        return pop_ele

def decimal_to_binary(n):
    if n == 0:
        print(0)
        return
    while n > 0:
        ans = n % 2
        push(ans)
        n //= 2
    display()

def display():
    global top
    for i in range(top, -1, -1):
        print(stack[i], end='')  
    print() 

decimal_to_binary(10)  
