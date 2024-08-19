'''
def change_case(text,style):
   if(style=="C" or style=="c"):
      y=[]
      text_list=list(text)
      for ele in text_list:
         if(65<= ord(ele) <=90):
            y.append(ele)
         elif(97<= ord(ele) <=112):
            y.append(chr(ord(ele)-32))
         else:
            y.append(ele)
      return "".join(y)      
   if(style=="S" or style=="s"):
      y=[]
      text_list=list(text)
      for ele in text_list:
         if(65<= ord(ele)<= 90):
            y.append(chr(ord(ele)+32))
         elif(97<= ord(ele) <=112):
            y.append(ele)
         else:
            y.append(ele)
      return "".join(y)
   if(style=="R" or style=="r"):
      y=[]
      text_list=list(text)
      for ele in text_list:
         if(65<= ord(ele)<= 90):
            y.append(chr(ord(ele)+32))
         elif(97<= ord(ele)<= 112):
            y.append(chr(ord(ele)-32))
         else:
            y.append(ele)
      return "".join(y)      
   if(style=="Z" or style=="z"):
      y=[]
      text_list=list(text)
      if(65<= ord(text_list[0])<= 90):
         for i in range(len(text_list)):
            if i%2==0:
               y.append()
    '''
  
  
  
  
'''  
def change_case(text, style):
    if style in ("C", "c"):  
        y = []
        for ele in text:
            if 'a' <= ele <= 'z':  
                y.append(chr(ord(ele) - 32))  
            else:
                y.append(ele) 
        return "".join(y)
    
    elif style in ("S", "s"):  
        y = []
        for ele in text:
            if 'A' <= ele <= 'Z':  
                y.append(chr(ord(ele) + 32))  
            else:
                y.append(ele)  
        return "".join(y)
    
    elif style in ("R", "r"):  
        y = []
        for ele in text:
            if 'A' <= ele <= 'Z':  
                y.append(chr(ord(ele) + 32))  
            elif 'a' <= ele <= 'z':  
                y.append(chr(ord(ele) - 32))  
            else:
                y.append(ele)  
        return "".join(y)
    
    elif style in ("Z", "z"):  
        y = []
        for i, ele in enumerate(text):
            if 'A' <= ele <= 'Z':  
                if i % 2 == 0:  
                    y.append(ele if 'A' <= text[0] <= 'Z' else chr(ord(ele) + 32))  
                else:  # Odd index
                    y.append(chr(ord(ele) + 32) if 'A' <= text[0] <= 'Z' else ele)
            elif 'a' <= ele <= 'z':  
                if i % 2 == 0:  # Even index
                    y.append(ele if 'a' <= text[0] <= 'z' else chr(ord(ele) - 32)) 
                else:  # Odd index
                    y.append(chr(ord(ele) - 32) if 'a' <= text[0] <= 'z' else ele)
            else:
                y.append(ele)  
        return "".join(y)
    
    else:
        return "Invalid style"


print(change_case("Utkarsh", "c"))  
print(change_case("uTkarsh", "S"))  
print(change_case("Utkarsh","r"))
print(change_case("utkarsh","Z"))
print(change_case("@#12utkaV","c"))
    
    
'''

def change_case(text, style):
    if style in ("C", "c"):  
        y = []
        for ele in text:
            if 'a' <= ele <= 'z':  
                y.append(chr(ord(ele) - 32))  
            else:
                y.append(ele) 
        return "".join(y)
    
    elif style in ("S", "s"):  
        y = []
        for ele in text:
            if 'A' <= ele <= 'Z':  
                y.append(chr(ord(ele) + 32))  
            else:
                y.append(ele)  
        return "".join(y)
    
    elif style in ("R", "r"):  
        y = []
        for ele in text:
            if 'A' <= ele <= 'Z':  
                y.append(chr(ord(ele) + 32))  
            elif 'a' <= ele <= 'z':  
                y.append(chr(ord(ele) - 32))  
            else:
                y.append(ele)  
        return "".join(y)
    
    elif style in ("Z", "z"):  
        y = []
        for i, ele in enumerate(text):
            if 'A' <= ele <= 'Z':  
                if i % 2 == 0:  
                    y.append(ele if 'A' <= text[0] <= 'Z' else chr(ord(ele) + 32))  
                else:  # Odd index
                    y.append(chr(ord(ele) + 32) if 'A' <= text[0] <= 'Z' else ele)
            elif 'a' <= ele <= 'z':  
                if i % 2 == 0:  # Even index
                    y.append(ele if 'a' <= text[0] <= 'z' else chr(ord(ele) - 32)) 
                else:  # Odd index
                    y.append(chr(ord(ele) - 32) if 'a' <= text[0] <= 'z' else ele)
            else:
                y.append(ele)  
        return "".join(y)

    elif style == "zigzag2":  
        y = []
        for i, ele in enumerate(text):
            if 'A' <= ele <= 'Z':
                if i % 2 == 0:  
                    y.append(chr(ord(ele) + 32))  
                else:
                    y.append(ele)  
            elif 'a' <= ele <= 'z':
                if i % 2 == 0:  
                    y.append(ele)  
                else:
                    y.append(chr(ord(ele) - 32))  
            else:
                y.append(ele)  
        return "".join(y)

    else:
        return "Invalid style"


print(change_case("Utkarsh", "c"))  
print(change_case("uTkarsh", "S"))  
print(change_case("Utkarsh", "r"))
print(change_case("utkarsh", "Z"))
print(change_case("@#12utkaV", "c"))
print(change_case("utkarsh", "zigzag2"))
print(change_case("UTKARSH", "zigzag2"))

    
         
            
            
            
            
            
    
      
