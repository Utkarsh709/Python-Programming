import random
def guess_number():
   rand_value=random.randint(1,20)
   guess_value=int(input("Guess number between 1 to 20:"))
   if 1 <= guess_value <=20:
      if guess_value==rand_value:
         print("congratulations you won")
      else:
         print("Better Luck next time")
   else:
      print("you enterd invalid number")
      
      
guess_number()  


      
   
   
