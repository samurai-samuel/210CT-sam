Too_high,Too_low = 20000,1   # shown here is the range of the guessing game


print("Think of a number between 1 and 20000") # prints to screen first 

bisection = True
while bisection:                      #while loop that continues to loop until 'y' is entered
    guess = (Too_high + Too_low)//2 # used floor division here so the number is always whole 
    print("Is your secret number", guess) # programme asks if this is the correct value with each iteration

    feedback = input( "Enter h if too high, l if too low and y if correct") # input for user 



    if feedback  == "h":      # conditional statements that are within the while loop
        Too_high = guess

    elif feedback == "l":
        Too_low = guess    #changes the value within the bracket

    elif feedback == "y":
        print("Your number was", guess)
        break                         # if the corect number is guessed programme prints value and then ceases

    else:
     print("incorrect input detected please enter h, y or l") # this conditional continues the loop so the programme does not have to be rerun
     continue










                      
