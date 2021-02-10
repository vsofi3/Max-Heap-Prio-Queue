# Max-Heap-Prio-Queue
For this lab, we will be taking what we’ve learned so far up a notch and learning how to
implement a max-heap priority queue. Priority queues are another commonly used Abstract Data
Type (ADT) due to the fact that they are self-sorting (they sort themselves) and that their time
complexity ranges from constant O(1) to linear O(n) depending on the operation and how they
are implemented. Our central task for this lab is to implement the max-heap variety of priority
queues.
Core Tasks:
1. Write the PriorityQueue class.
Program Requirements:
Task 1: Write the priority queue class.
For task 1, you will need to write a PriorityQueue class. The class is detailed as follows:
• __𝑖𝑛𝑖𝑡__(self, capacity) → 𝑵𝒐𝒏𝒆
o Complexity: O(1)
o Valid Input: An integer in (0, ∞]. Use a default, valid capacity on invalid input.
o Description: This is the constructor for the class. You will need to create the
following instance variables here:
▪ A variable _maxSize
▪ A variable _currentSize
▪ A variable _heap (contains an empty list)
▪ Any other instance variables you want.
• __𝑠𝑡𝑟__(self) → 𝒔𝒕𝒓𝒊𝒏𝒈
o Complexity: O(n)
o Description: The string method returns a string representation of the queue. Use
the function provided in the main.
• enqueue(self,𝑡𝑖𝑐𝑘𝑒𝑡) → 𝑩𝒐𝒐𝒍𝒆𝒂𝒏
o Complexity: O(lg(n))
o Valid Input: An object of type: MealTicket. Return False on invalid input.
o Description: This method will add a ticket to the queue based on its priority.
▪ Note 1: The priority of a ticket is determined by its ID.
▪ Note 2: When adding a node to your heap, remember that for every node
n, the value in n must be greater than or equal to the values of its children,
but your heap must also maintain the correct shape. (i.e., for any node
there can be at most two children, and the parent has a greater priority
than all subsequent nodes.)
• dequeue𝑀𝑎𝑥(self) → 𝑩𝒐𝒐𝒍𝒆𝒂𝒏|𝑴𝒆𝒂𝒍𝑻𝒊𝒄𝒌𝒆𝒕
o Complexity: O(n lg(n)) or less
o Description: This this method will remove and return the ticket with the highest
priority. If the queue is empty, then it will return False.
• peekMax(self) → 𝑭𝒂𝒍𝒔𝒆|𝑴𝒆𝒂𝒍𝑻𝒊𝒄𝒌𝒆𝒕
o Complexity: O(1)
o Description: This method lets the user peak at the ticket with the highest priority
without removing it from the queue. Returns false if the queue is empty.
• 𝑖𝑠𝐸𝑚𝑝𝑡𝑦(self) → 𝑩𝒐𝒐𝒍𝒆𝒂𝒏
o Complexity: O(1)
o This method will return True or False depending on if the queue is empty or not.
• 𝑖𝑠𝐹𝑢𝑙𝑙(self) → 𝑩𝒐𝒐𝒍𝒆𝒂𝒏
o Complexity: O(1)
o This method will return True or False depending on if the queue is full or not.
Note 1: The methods listed above are the only methods that will be tested. However, you may
add additional methods as you please. I would recommend the following:
• _heapify – to restructure your heap.
• _swap – to swap parent and child nodes.
• _getParent – to get the parent nodes index.
Note 2: See Figure 1 at the bottom of this section for a sample test run of the Queue class. The
provided main can be used to achieve this exact output which may be helpful for testing.
Note 3: Pay attention to the complexity bounds mentioned in the method descriptions. Your
implementation must run within these bounds.
Note 4: For this assignment you must use a list to implement your heap. The use any other builtins data structures are explicitly forbidden. Using them will result in a 0 for the assignment. The
same goes for method annotations (e.g. def isEmpty(self) -> int:).
Extra Credit: If you are looking for general bonus points (10%): Implement heap-sort (you will
already have a max-heapify). The details of this method are given below:
• heap_sort(self, array) → 𝑩𝒐𝒐𝒍𝒆𝒂𝒏|𝑳𝒊𝒔𝒕
o Complexity: O(n lg(n))
o Valid Input: A list of MealTickets. Return False on invalid input.
o Description: This method will sort the given list of MealTickets.
▪ Note 1: Extra credit is all or nothing.
I/O Specifications and Program Robustness:
For this assignment 2 files are provided: lab2-main.py and mealticket.py. You are free to use the
main provided or to make your own. Inside the main you will find the method for the __str__
class. Copy-paste this method. Your string output must be exact, so use this method.
Warning: I will be testing your code with a more robust main that will check all of the corner
cases and uses a wider variety of tickets. Keep this in mind while developing your data 
structures. The provided main tests some of the corner cases but not all of them. You will need to
use the methodology discussed in lab to figure out all corner cases and account for them. Your
programs must be robust (i.e. crash on bad input or calls).
