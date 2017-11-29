def armstrong(value):
 
 result = 0           #The result must be made to equal zero so that when Iadd it in the for loop it does not affect  
 for d in value:
     result += int(d)**3 # The for loop runs through and each numberand then cubes them and adds them
 if result == int(value):

   return True  #booleans here used in conjuction wih return statement work with the stored value passed from the arguments.

 else:
   return False
            
     
value = input("Please enter a 3 digit number") # having an input here means I do not have to type the function and then the value.
result = armstrong(value)
if result == True:
    print("Yes")         #if the value is an armstrong number then Yes is printed

else:
    print("No")

