#rotate the element of an array (left and right)
def left_rotation(arr,d):
    n=len(arr)
    d=d%n
    return arr[d:] + arr[:d]
    
def right_rotation(arr,d):
    n=len(arr)
    d=d%n
    return arr[-d:] + arr[:-d]

arr=[1,2,3,4,5]
d=2
print(left_rotation(arr,d))
print(right_rotation(arr,d))
