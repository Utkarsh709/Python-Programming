def get_even_odd_count1(L):
   even,odd=0,0
   for ele in L:
      if ele%2==0:
         even+=1
      else:
         odd+=1
   return even,odd      
   
def eo_1():
   return get_even_odd_count1([1,2,3,4,5,6,7,8,9,10])
 


def get_even_odd_count2(L):
   even,odd=0,0
   for ele in L:
      t=ele%2
      even+=1-t
      odd+=t

def eo_2():
   return get_even_odd_count2([1,2,3,4,5,6,7,8,9,10])
   
   
      
      
def get_even_odd_count3(L):
   even,odd=0,0
   for ele in L:
      if ele%2:
         odd+=1
      else:
         even+=1

def eo_3():
   return get_even_odd_count3([1,2,3,4,5,6,7,8,9,10])
      
      


import time
def check_performance3(approaches):
   time_taken=[]
   for approach in approaches:
      time_take=[]
      for i in range(200):
         start_time=time.time()
         approach()
         end_time=time.time()
         time_take.append(end_time-start_time)
      time_taken.append(sum(time_take)/200)
   return time_taken  
   


print(check_performance3(os_1,os_2,os_3))

