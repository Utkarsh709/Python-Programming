# find the median of given array
num=[-9,0,-3,2,1,6,4,-1,4,77,8,9]
num_sort=sorted(num)
if len(num)%2!=0:
    print("median:",num_sort[len(num_sort)//2])
else:
    k=num_sort[(len(num_sort)//2)-1] + num_sort[(len(num_sort)//2)+1]
    print("median:",k//2)



  


