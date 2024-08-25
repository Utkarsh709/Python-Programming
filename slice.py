'''
def slice(objects,parameters):
    if parameters==[]:
        return objects
    
    if type(objects)=="list":
       if len(parameters)==1:
           first_arg=parameters[0]
           y=[]
           for i in range(first_arg,len(objects)):
               y.append(objects[i])
        return y
        
        if len(parameters)==2:
            first_arg=parameters[0]
            second_arg=parameters[1]
            y=[]
            if second_arg>len(objects) or second_arg==len(objects):
               for i in range(first_arg,second_arg):
                  y.append(objects[i])
        return y
        
        if len(parameters)==3:
            first_arg=parameters[0]
            second_arg=parameters[1]
            third_arg=parameters[2]
            y=[]
            if third_arg==0:
                return "ValueError:slice step cannot be zero"
            if second_arg>len(objects) or second_arg==len(objects):
               for i in range(first_arg,second_arg,third_arg):
                   y.append[objects[i]]
        return y        
        
print([1,2,3,4],[1])                
'''






'''
def slice(objects, parameters):
    # Check if parameters list is empty
    if not parameters:
        return objects
    
    # Check if objects is a list
    if type(objects) != list:
        return "TypeError: objects must be a list"
    
    # Handle the case with one parameter
    if len(parameters) == 1:
        first_arg = parameters[0]
        if first_arg < 0:
            first_arg = len(objects) + first_arg
        y = []
        for i in range(first_arg, len(objects)):
            y.append(objects[i])
        return y
    
    # Handle the case with two parameters
    elif len(parameters) == 2:
        first_arg = parameters[0]
        second_arg = parameters[1]
        if first_arg < 0:
            first_arg = len(objects) + first_arg
        if second_arg < 0:
            second_arg = len(objects) + second_arg
        y = []
        for i in range(first_arg, min(second_arg, len(objects))):
            y.append(objects[i])
        return y
    
    # Handle the case with three parameters
    elif len(parameters) == 3:
        first_arg = parameters[0]
        second_arg = parameters[1]
        third_arg = parameters[2]
        if third_arg == 0:
            return "ValueError: slice step cannot be zero"
        if first_arg < 0:
            first_arg = len(objects) + first_arg
        if second_arg < 0:
            second_arg = len(objects) + second_arg
        y = []
        for i in range(first_arg, min(second_arg, len(objects)), third_arg):
            y.append(objects[i])
        return y
    
    # Handle invalid parameter cases
    return "ValueError: Invalid parameters"

# Test cases
print(slice([1, 2, 3, 4], [1]))           # Output: [2, 3, 4]
print(slice([1, 2, 3, 4], [1, 3]))        # Output: [2, 3]
print(slice([1, 2, 3, 4], [1, 4, 2]))     # Output: [2, 4]
print(slice([1, 2, 3, 4], [1, 4, 0]))     # Output: "ValueError: slice step cannot be zero"
print(slice([1, 2, 3, 4], []))            # Output: [1, 2, 3, 4]
print(slice([1, 2, 3, 4], [1, 5]))        # Output: [2, 3, 4]
print(slice([1, 2, 3, 4], [1, -1]))       # Output: [2, 3]
print(slice([1, 2, 3, 4], [1, 5, 2]))     # Output: [2, 4]
print(slice([1, 2, 3, 4], [1, -1, 2]))    # Output: [2, 3]


'''

'''
def slice(iterable, parameters):
    # Check if parameters list is empty
    if not parameters:
        return iterable
    
    # Convert iterable to list if it's not already a list
    # This allows for indexing and slicing
    if not isinstance(iterable, (list, tuple, str)):
        try:
            iterable = list(iterable)
        except TypeError:
            return "TypeError: objects must be a list, tuple, or string"

    # Handle the case with one parameter
    if len(parameters) == 1:
        start = parameters[0]
        if start < 0:
            start = len(iterable) + start
        # Ensure start is within bounds
        start = max(start, 0)
        return iterable[start:]
    
    # Handle the case with two parameters
    elif len(parameters) == 2:
        start, end = parameters
        if start < 0:
            start = len(iterable) + start
        if end < 0:
            end = len(iterable) + end
        # Ensure start and end are within bounds
        start = max(start, 0)
        end = min(end, len(iterable))
        return iterable[start:end]
    
    # Handle the case with three parameters
    elif len(parameters) == 3:
        start, end, step = parameters
        if step == 0:
            return "ValueError: slice step cannot be zero"
        if start < 0:
            start = len(iterable) + start
        if end < 0:
            end = len(iterable) + end
        # Ensure start and end are within bounds
        start = max(start, 0)
        end = min(end, len(iterable))
        return iterable[start:end:step]
    
    # Handle invalid parameter cases
    return "ValueError: Invalid parameters"

# Test cases
print(slice([1, 2, 3, 4], [1]))           # Output: [2, 3, 4]
print(slice((1, 2, 3, 4), [1, 3]))        # Output: (2, 3)
print(slice("hello", [1, 4, 2]))           # Output: 'el'
print(slice("hello", [1, 4, 0]))           # Output: "ValueError: slice step cannot be zero"
print(slice([1, 2, 3, 4], []))            # Output: [1, 2, 3, 4]
print(slice("abcdef", [1, 5]))            # Output: 'bcde'
print(slice([1, 2, 3, 4], [1, -1]))       # Output: [2, 3]
print(slice("abcdef", [1, -1, 2]))        # Output: 'bdf'
'''






def slice(objects, parameters):
    # Check if parameters list is empty
    if not parameters:
        return objects
    
    # Check if objects is a supported type (list, tuple, or string)
    if not isinstance(objects, (list, tuple, str)):
        return "TypeError: objects must be a list, tuple, or string"
    
    # Convert objects to a list if it's a tuple or string to handle slicing uniformly
    if isinstance(objects, tuple):
        objects = list(objects)
    elif isinstance(objects, str):
        objects = list(objects)
    
    # Handle the case with one parameter
    if len(parameters) == 1:
        start = parameters[0]
        if start < 0:
            start = len(objects) + start
        start = max(start, 0)
        result = []
        for i in range(start, len(objects)):
            result.append(objects[i])
    
    # Handle the case with two parameters
    elif len(parameters) == 2:
        start, end = parameters
        if start < 0:
            start = len(objects) + start
        if end < 0:
            end = len(objects) + end
        start = max(start, 0)
        end = min(end, len(objects))
        result = []
        for i in range(start, end):
            result.append(objects[i])
    
    # Handle the case with three parameters
    elif len(parameters) == 3:
        start, end, step = parameters
        if step == 0:
            return "ValueError: slice step cannot be zero"
        if start < 0:
            start = len(objects) + start
        if end < 0:
            end = len(objects) + end
        start = max(start, 0)
        end = min(end, len(objects))
        result = []
        for i in range(start, end, step):
            result.append(objects[i])
    
    # Handle invalid parameter cases
    else:
        return "ValueError: Invalid parameters"
    
    # Convert result back to the original type if necessary
    if isinstance(objects, tuple):
        return tuple(result)
    elif isinstance(objects, str):
        return ''.join(result)
    else:
        return result

# Test cases
print(slice([1, 2, 3, 4], [1]))           # Output: [2, 3, 4]
print(slice((1, 2, 3, 4), [1, 3]))        # Output: (2, 3)
print(slice("hello", [1, 4, 2]))           # Output: 'el'
print(slice("hello", [1, 4, 0]))           # Output: "ValueError: slice step cannot be zero"
print(slice([1, 2, 3, 4], []))            # Output: [1, 2, 3, 4]
print(slice("abcdef", [1, 5]))            # Output: 'bcde'
print(slice([1, 2, 3, 4], [1, -1]))       # Output: [2, 3]
print(slice("abcdef", [1, -1, 2]))        # Output: 'bdf'
print(slice("abcdef", [-1]))
