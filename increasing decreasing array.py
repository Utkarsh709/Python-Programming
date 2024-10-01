# Rearrange the array in increasing and decreasing order
num = [4, 6, 5, -9, 3, 0, 2]
sorted_num = sorted(num)
k = len(sorted_num) // 2  
first = sorted_num[:k]  
if len(sorted_num) % 2 == 0:
    mid = None 
    second = sorted_num[k:]  
else:
    mid = sorted_num[k]  
    second = sorted_num[k+1:]
second_reversed = list(reversed(second))
new = []
for i in range(len(first)):
    new.append(first[i])
    new.append(second_reversed[i])
if mid is not None:
    new.append(mid)
print("Rearranged array:", new)
