alpha ={'a','b'}
def dfa_endswith_b(text):
   final_states={Q1}
   result=Q0(text)
   if result in final_states:
      return "Accepted"
   else:
      return "Rejected"
 
 
def Q0(text):
   if len(text)>0:
      symbol=text[0]
      if symbol in alpha:
         if symbol=='b':
            return Q1(text[1:])
         else:
            return Q0(text[1:])
      else:
         return "Rejected"
   
   
   else:
      return Q0
      
      
 
def Q1(text):
   if len(text)>0:
      symbol=text[0]
      if symbol in alpha:
         if symbol=='b':
            return Q1(text[1:])
         else:
            return Q0(text[1:])
      else:
         return "Rejected"
    
   else:
      return Q1
      
 

print(dfa_endswith_b("aabaaab"))
