top = -1
size = 20
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

def bracket_check(expression):
    global top
    for ele in expression:
        if ele in ['[', '{', '(', '<']:
            push(ele)
        elif ele in [']', '}', ')', '>']:
            if top == -1:  
                return False
            open_bracket = pop()
            if (ele == ']' and open_bracket != '[') or \
               (ele == '}' and open_bracket != '{') or \
               (ele == ')' and open_bracket != '(') or \
               (ele == '>' and open_bracket != '<'):
                return False

    return top == -1  

s = "[()]{}{[()()]()}"
print(bracket_check(s))
