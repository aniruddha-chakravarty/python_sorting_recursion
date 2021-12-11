# Towers of Hanoi, recursive. 

Algorithm: 

As we can solve for n-1 in recursive cases, instead of breaking down problem for 3 discs, we solve it for n-1 or 3-1 = 2 discs.

Step 1: Take n-1 disc from start to aux tower.

Step 2: Move nth disc from start tower to destination tower. 

Step 3: Move n-1th disc from aux to destination tower. 

