#Find maximum product subarray in an array
import numpy as np
num=[3,4,-6,3,1,7,4]
subarrays=[]
for i in range(len(num)):
    for j in range(i+1,len(num)+1):
        subarray=num[i:j]
        subarrays.append(subarray)
subarrays_prod=[]        
for ele in subarrays:
    subarrays_prod.append(np.prod(ele))
max_ele=max(subarrays_prod)
max_idx=subarrays_prod.index(max_ele)
print(subarrays[max_idx])
    
    