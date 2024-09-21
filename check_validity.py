symbols={'{','[','<','(',')','>',']','}' }
pairs={'{':'}','[':']','<':'>','(':')'}
def check_validity(text):
   stack=[]
   for symbol in text:
      if symbol in symbols:
         if symbol in pairs:
            stack.append(symbol)
         else:
            if (pairs[stack[-1]]==symbol):
               stack.pop()
            else:
               return "Invalid String"      
      else:
         return "Invalid String"
      
print(check_validity("(<>)"))
print(check_validity("(a)"))
      
