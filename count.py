'''
def count(string,sub_string,boolean):
   if (sub_string=="" and boolean==True):
     return len(string)
   elif (sub_string=="",boolean==False) or (sub_string==""):
     return len(string)+1
   elif (sub_string==" ") or (sub_string==" " and boolean==False):
     return 0
   elif (sub_string!=" " and boolean==False):
     def count_F(string,sub_string):
         count__f=0
         if (string.find(sub_string))==1:
              k=string.index(sub_string)
              k_string=string[:k]+string[k:]
              count__f+=1
              if (string.find(sub_string))!=1:
                  count_F(string,k_string)
         else:
           return count__f
   else:
      if (sub_string!=" " and boolean==True):
        return len(sub_string)+1
        
print(count("sggs","gg","False"))        
        
 '''
 
def count(string, sub_string, boolean):
    if sub_string == "" and boolean:
        return len(string)
    elif sub_string == "" and not boolean:
        return len(string) + 1
    elif sub_string == " ":
        return 0
    elif sub_string != " " and not boolean:
        def count_F(s, sub_s):
            count_f = 0
            start = 0
            while True:
                start = s.find(sub_s, start)
                if start == -1:
                    break
                count_f += 1
                start += len(sub_s)  # Move to the next character after the current match
            return count_f
        
        return count_F(string, sub_string)
    elif sub_string != " " and boolean:
        return len(sub_string) + 1

# Test the function
print(count("sggs", "gg", False))
 
     
     
     
     
