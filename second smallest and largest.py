num = [-4, -8, 0, 6, 2, 8, 4, 3]

# Initialize variables to track the first and second smallest and largest numbers
first_smallest = float('inf')
second_smallest = float('inf')
first_largest = float('-inf')
second_largest = float('-inf')

for ele in num:
    # Update the smallest numbers
    if ele < first_smallest:
        second_smallest = first_smallest  # Update second smallest before changing first
        first_smallest = ele
    elif ele < second_smallest and ele != first_smallest:
        second_smallest = ele

    # Update the largest numbers
    if ele > first_largest:
        second_largest = first_largest  # Update second largest before changing first
        first_largest = ele
    elif ele > second_largest and ele != first_largest:
        second_largest = ele

print("First smallest:", first_smallest)
print("Second smallest:", second_smallest)
print("First largest:", first_largest)
print("Second largest:", second_largest)
