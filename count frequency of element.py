#count the frequency of each element in an array
num=[1,2,3,2,4,4,2,1,0,7,5,5,5,4]
dic={}
for ele in num:
    dic[ele]=num.count(ele)
print(dic)    
    