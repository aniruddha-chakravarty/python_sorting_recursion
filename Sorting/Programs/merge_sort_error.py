def merge_sort(arr): 
  
  if len(arr) > 1:
    left_arr = arr[:len(arr) // 2] #calculates length, divides by integer , gets floor int  value from index zero
    right_arr = arr[len(arr) // 2:]  #calculates length, divides by 2  integer ,  gets floor int  value from last index 
    merge_sort(left_arr) #recursion 
    merge_sort(right_arr) #recursion
    
  #use index i to keep track of leftmost element in left array, and j to keep track of leftmost element in right array and k keeps track of index in merged array
  
  
  i = 0 #left array index
  
  j = 0 # right array index
  
  k = 0 #merged array index 
  
  while i < len(left_arr) and j < len(right_arr): 
    if left_arr[i] < right_arr[j]: 
      arr[k] = left_arr[i]
      i += 1
   
    else: 
      
      arr[k] = right_arr[j]
      j += 1
      
    k += 1 
    
    while i < len(left_arr): 
      arr[k]= left_arr[i]
      i += 1 
      k += 1 
      
    while j < len(right_arr): 
      arr[k]= right_arr[j]
      j += 1 
      k += 1 
      
      
        
      
    # for case 
      

  
  
  


arr_test = ['2', "4", "5", "3", "9", "8"]

merge_sort(arr_test)

print(arr_test)