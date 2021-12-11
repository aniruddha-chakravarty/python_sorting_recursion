# sum of n natural numbers

def sum_recursion(n): 
  if  n <= 1: 
    return n
  else:
    return n + sum_recursion(n-1)
    
#Driver code

n = 22

if n < 0: 
  print("Enter +ve number")
else: 
   print("Sum of n natural numbers is: ", sum_recursion(n))
    
  