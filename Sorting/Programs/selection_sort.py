def selection_sort(arr): 
  for i in range(0, len(arr) -1): #can skip the last index here, by the time iteration reaches there, rest of array will be sorted
    curr_min_index = i 
    
    for j in range(i+1, len(arr)):
      if arr[j] < arr[curr_min_index]: 
        curr_min_index = j 
    
    #swap operation, at this point we're pointing to smallest within unsorted array
    arr[i] , arr[curr_min_index] = arr[curr_min_index], arr[i]
    
    
    
#driver unicode
arr = [2, 8, 4, 5, 3, 7 ]

selection_sort(arr)

print(arr)
    