#remove duplicate from sorted array
num=[1,2,3,4,3,4,5,6,3,1]
y=[]
for ele in num:
    if ele not in y:
        y.append(ele)
print(y)        