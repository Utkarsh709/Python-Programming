#add element in array

#method1
num=[1,2,3,3,4]
num.insert(2,60)
print(num)

#method2
new=[]
pos=int(input("enter a position:"))
element=int(input("enter a element to be inserted:"))
for i in range(len(num)):
    if i==pos-1:
        new.append(element)
    else:
        new.append(num[i])
print(num)        
        