#find all repeating and non repeating element in an array
num=[1,2,3,4,4,3,5,6,7,8]
repeat=[]
non_repeat=[]
for ele in num:
    if num.count(ele)>1:
        if ele not in repeat:
            repeat.append(ele)
    else:
        non_repeat.append(ele)
print("repeat:",repeat)
print("non-repeat:",non_repeat)