num = [3, 4, 5, 5, 2, 1, 3, 4, 1, 2, 3, 3, 3, 7]

# Step 1: Count the frequency of each element
frequency = {}
for ele in num:
    if ele in frequency:
        frequency[ele] += 1
    else:
        frequency[ele] = 1

# Step 2: Create a list of tuples (element, frequency)
frequency_list = [(key, value) for key, value in frequency.items()]
print(frequency_list)

# Step 3: Sort the frequency list by frequency and then by element value
frequency_list.sort(key=lambda x: (x[1], x[0]))

# Step 4: Create the sorted result based on frequency
result = []
for ele, count in frequency_list:
    result.extend([ele] * count)

print(result)
