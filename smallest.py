num = [4, 6, 5, -9, 3, 0, 2]
smallest_num = num[0]  # Start with the first element

for ele in num:
    if ele < smallest_num:
        smallest_num = ele

print("Smallest number is:", smallest_num)
