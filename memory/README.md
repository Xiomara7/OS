Instructions:

Write a simulation of the Optimal Replacement Algorithm, Second Chance Algorithm, 
and WorkingSetClock Page Replacement Algorithm (WSCPRA) as described in our operating 
system textbook: Modern Operating Systems by Andrew Tanenbaum.

*** 

optimal.py: 

Each page contains a reference bit to indicate if it's referenced or not. Also, they 
contains a modified bit to indicate if it's has been modified. At the moment that a 
page fault occurs, some set of pages is in memory. One of these pages will be referenced 
on the next instructions. Other pages may not be referenced until later. The optimal 
algorithm says that the farthest page should be removed. 


second.py:

Each page contains a reference bit to indicate if it's referenced or not. Also, they 
contains a modified bit to indicate if it's has been modified. If the reference bit is 0, 
the page is referenced, so it is replaced immediately, all the elements will be shifted to
the left and the new item will be inserted at the end of the list. If the reference bit is 
1, the bit is cleared, the page is put into the end of the list of pages and the search 
continues. 

wsclock.py: 

Initially, the list is empty as well in the others. When the first page is loaded, it is 
added to the list. As more pages are added, they go into the list to form a ring. Each 
page contains the time of last use, as well as the reference and modified bits. if the 
reference bit is 1, the page has been used during the current time so it's not an ideal 
item to remove. If the reference is 0, check if the age is greater than tau. If both are 
true, the page is claimed and the new item will be put in there and now the arrow will be 
move to the next item. 

*** 

**I discussed the algorithms with my classmates, including Julio de la Cruz and Luis 
Albertorio**


