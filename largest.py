num = [4, 6, 5, -9, 3, 0, 2]
largest_num = float('-inf')  # Start with negative infinity

for ele in num:
    if ele > largest_num:
        largest_num = ele

print("Largest number is:", largest_num)
