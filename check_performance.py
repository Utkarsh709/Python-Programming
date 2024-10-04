def factorial_1(num):
   fact1=1
   if num <2:
      return fact1
   else:
      for i in range(2,num+1):
         fact1=fact1*i
      return fact1   
      
      
def factorial_2(num):
   fact2=1
   if num>2:
      for i in range(2,num+1):
         fact2=fact2*i
      return fact2
   else:
      return fact2
      
  
def f1():
   x=[]
   for i in range(1,1000,2):
      x=factorial_1(i)
      

def f2():
   y=[]
   for i in range(1,1000,1):
      y=factorial_2(i)
      
      
import time
def check_performance(approaches):
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
   
 
print(check_performance([f1,f2])) 
 

   
