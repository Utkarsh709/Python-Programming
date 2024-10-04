def count_text(L):
   result = []
   for element in L:
      if isinstance(element, (list, tuple, set)):
         result.append(count_text(list(element)))
      if isinstance(element, str):
         s = 'aeiou'
         if all(v not in element for v in s):  
            result.append(element)
         else:
            vowels = ['a', 'e', 'i', 'o', 'u']
            vowels_bool = []
            idx = []
            for char in element:
               if char in vowels:
                  vowels_bool.append(True)
               else:
                  vowels_bool.append(False)
            for i in range(len(vowels_bool)):
               if vowels_bool[i] == True:
                  idx.append(vowels[i])  
            vowels_count = []
            for ele in idx:
               vowels_count.append(element.count(ele))
            if sum(vowels_count) == len(vowels_count): 
               result.append(element)
   return len(result)

def c():
   return count_text(['aeiou', (12, 'ak'), {'utkarsh', (12, 'omk')}])


def count_text1(L):
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for element in L:
        if isinstance(element, (list, tuple, set)):
            result.append(count_text(list(element)))
        if isinstance(element, str):
            vowel_count = {v: 0 for v in vowels}
            for char in element:
                if char in vowel_count:
                    vowel_count[char] += 1
            if all(count == 0 for count in vowel_count.values()):
                result.append(element)
            else:
                non_zero_counts = [count for count in vowel_count.values() if count > 0]
                if len(set(non_zero_counts)) == 1:
                    result.append(element)
    
    return len(result)


 

def c1():
   return count_text1(['aeiou', (12, 'ak'), {'utkarsh', (12, 'omk')}])
import time
def check_performance2(approaches):
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


   
   
y=check_performance2([c,c1])  
# traditional y[0]
# proposed  y[1]
if y[0]>y[1]:
   print("Performance increases")
   print(abs((y[0]-y[1])/y[0])*100)
elif y[0]==y[1]:
   print("performance same")
else:
   print("performance decreases")
   print(abs((y[1]-y[0])/y[1])*100)
   
   
   
   
