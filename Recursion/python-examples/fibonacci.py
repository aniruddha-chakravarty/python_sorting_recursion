# fibonacci 

def fibonacci_recursion(n): 
  if  n <= 1: 
    return n
  else:
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
    
#Driver code

num = 4

if num < 0: 
  print("Enter +ve number")
else: 
   print("factorial of n natural numbers is: ")
   for i in range (num):
     print(fibonacci_recursion(i))
    
  