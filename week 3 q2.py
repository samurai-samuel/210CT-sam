

def rec_lin(l, target):



    if not l: # if the integer is not in the list an error is raised
        print("not found")
       
    
    elif l[0]== target:  #returns the slice in which the number is
        return 0 and print("yes")
        
        
    
        
        
       
    else:
        return 1 + rec_lin(l[1:], target)  #recursive function
  


 
'''test being run'''

  
l =[3,5,7,1,2,9]
target =5                # test to locate number

print(rec_lin(l,5))

target =4               # test to raise error 

print(rec_lin(l,target))
     
    
    
