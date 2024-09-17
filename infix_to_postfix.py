#infix to postfix
size = 100  # Set a reasonable default size for the stack
stack = [None] * size
top = -1

def is_full():
    return top == size - 1

def is_empty():
    return top == -1

def push(n):
    global top
    global stack
    if is_full():
        print("Overflow")
    else:
        top += 1
        stack[top] = n
       
def pop():
    global top
    global stack
    if is_empty():
        print("Underflow")
        return None
    else:
        pop_ele = stack[top]
        top -= 1
        return pop_ele
       
def peek():
    global top
    global stack
    if is_empty():
        return None
    else:
        return stack[top]

def precedence(char):
    if char == "^" or char == "$":
        return 3
    if char == "/" or char == "*":
        return 2
    if char == "+" or char == "-":
        return 1
    return 0

def infix_to_postfix(exp):
    result = []
    for ele in exp:
        if 'a' <= ele <= 'z':  # Operands (variables)
            result.append(ele)
        elif ele in ["^", "$", "/", "*", "+", "-"]:  # Operators
            while (not is_empty() and precedence(ele) <= precedence(peek())):
                result.append(pop())
            push(ele)
        elif ele == "(":  # Left parenthesis
            push(ele)
        elif ele == ")":  # Right parenthesis
            while not is_empty() and peek() != "(":
                result.append(pop())
            pop()  # Remove the '(' from the stack
    while not is_empty():  # Pop all the operators left in the stack
        result.append(pop())
    return "".join(result)

print(infix_to_postfix("a+b/c*d"))  # Output should be "abc/d*+"