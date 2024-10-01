# Method 1: Using slicing
num = [1, 2, 3, 4, 5]
print("Reversed using slicing:", num[::-1])

# Method 2: Using a loop
num_reverse = []
for i in range(-1, -len(num)-1, -1):  # Corrected the range
    num_reverse.append(num[i])
print("Reversed using a loop:", num_reverse)
