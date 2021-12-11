# gcd

def gcd_recursion(x, y): 
  if y == 0: 
    return x
  else:
    return gcd_recursion(y, x % y)
    
#Driver code

x = 4
y = 2

if (x < 0) | (y < 0): 
  print("Enter +ve number")
else: 
   print(gcd_recursion(x, y))
  