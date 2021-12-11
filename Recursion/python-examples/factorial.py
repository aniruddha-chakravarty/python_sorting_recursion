# factorial of n natural numbers

def factorial_recursion(n): 
  if  n <= 1: 
    return n
  else:
    return n * factorial_recursion(n-1)
    
#Driver code

n = 4

if n < 0: 
  print("Enter +ve number")
else: 
   print("factorial of n natural numbers is: ", factorial_recursion(n))
    
  