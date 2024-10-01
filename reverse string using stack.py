x = "GeeksQuiz"
top = -1
size = len(x)
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
        
def rev_str(string):
    global top
    for ele in string:
        push(ele)
    
    reversed_string = ""
    while top != -1:
        reversed_string += pop()
        
    return reversed_string
      

print(rev_str(x))
