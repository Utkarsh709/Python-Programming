symbols = {'{', '[', '<', '(', ')', '>', ']', '}'}
pairs = {'{': '}', '[': ']', '<': '>', '(': ')'}
def check_validity1(text):
    if not isinstance(text, str):
        return None  
    stack = []
    for symbol in text:
        if symbol in symbols:
            if symbol in pairs:  
                stack.append(symbol)
            else:  
                if stack and pairs[stack[-1]] == symbol:
                    stack.pop()
                else:
                    return "Invalid String"
    if not stack:  
        return "Valid String"
    else:
        return "Invalid String"

def get_valid_invalid_text_counts(example):
    valid_count = 0
    invalid_count = 0
    for ele in example:
        if isinstance(ele, (set, tuple, list)):
            for item in ele:
                if isinstance(item, str):
                    if check_validity1(item) == "Valid String":
                        valid_count += 1
                    elif check_validity1(item) == "Invalid String":
                        invalid_count += 1
        elif isinstance(ele, str):
            if check_validity1(ele) == "Valid String":
                valid_count += 1
            elif check_validity1(ele) == "Invalid String":
                invalid_count += 1
    return valid_count, invalid_count

example = ['[{(', "()", ']]', "<()>", (), set(), 45, {'<>', 45, '({'}]
print(get_valid_invalid_text_counts(example))

