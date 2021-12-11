Quicksort: 

1] Choose pivot (either last or random)

2] Elements lower than pivot go to left subarray, greater go to right sub-array.

3] Call quick-sort recursively on left & right sub-arrays.

We have p as last. We iterate i towards pivot, for grreater. We iterate j away, for less. 

When i finds element greater than p, and j finds element less than p, then swap both. 

When j moves to left of i, sorting is done. Swap i and p. 

Elements left of new pivot are less than pivot, elements to right of pivot are greater. 

Recursively call quick sort within left and right sub-array. 

