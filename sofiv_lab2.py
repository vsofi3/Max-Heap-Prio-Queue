"""
Sofi Vinas
CIS 313 Lab 2
Implementing a Max-Heap Priority Queue
"""

from mealticket import *

#time complexity ranges from constant O(1) to linear O(n) depending on the
#operation and how they are implemented

#implement the max-heap variety of priority queues


#TODO: WRITE THE PRIORITY QUEUE CLASS


MAX_CAPACITY = 100
#Use default when invalid or incorrect input is given

class PriorityQueue():
    #DONE?
    def __init__(self, capacity): #user provides capacity for PrioQueue
        """
    Complexity: O(1)
    Valid input: An integer in (0, infinity]. Use a default valid capacity
        on invalid input
    Description: This is the constructor for the class. Used to make PriorityQueue
        instances. Create the following instance variables
        """
        #check to see if the user gave a positive int or valid input (any int)
        if(capacity <= 0 or type(capacity) is not int):
            self._maxSize = MAX_CAPACITY #use DEFAULT CAPACITY FOR BOGUS INPUT
        else:
            self._maxSize = capacity #use what the user provided
        self._currentSize = 0 #current size of priorityQueue is 0 because we just made it
        self._heap = [] #contains an empty list to put MealTickets in

    #DONE
    def __str__(self):
        """
            Author: Jared Hall
            Date: 01/03/2020
            Description: Output the current queue as a string.
            Inputs: None
            Outputs: str
        """
        returnValue = "Current queue: ["
        if (self._currentSize != 0):
            for ticket in self._heap: #iterating through items in heap-> O(n) complexity
                if (ticket is None):
                    break
                else:
                    returnValue += "(" + str(ticket.ticketID) + ", "
                    returnValue += str(ticket.totalCost) + "), "
            returnValue = returnValue[:-2] + "]"
        else:
            returnValue += "]"
        return returnValue

    #DONE
    def _swap(self, childPos, parentPos): #takes two integers (list indices)
        """
        Swap the posiitons of the childTicket and the parentTicket within the heap list
        :param childTicket:
        :param parentTicket:
        """
        #JUST LIKE SWAPPING TWO VALUES
        temporary = self._heap[childPos] #store the MealTicket of the childPosition of the heap in temporary
        self._heap[childPos] = self._heap[parentPos] #store the value of the parentPosition of the heap in the CHILDPOSITION
        self._heap[parentPos] = temporary #store the temporary value (childPos) in the parentPosition of the heap


    def _leftChild(self, position): #ZERO-BASED INDEXING
        return 2*position + 1

    def _rightChild(self, position): #ZERO-BASED INDEXING
        return 2*position + 2

    def _isLeaf(self, position):
        ret = False
        if(position) >= (self._currentSize // 2) and (position) <= self._currentSize:
            ret = True
        return ret

    def _getParent(self, index):
        #function to get the POSITION of PARENT of a MealTicket in the list
        #if((index > 0) and (index < self._currentSize)): #return parent MealTicket index
        return (index-1) // 2


    #DOUBLE CHECK
    def _heapify(self, position):
        """
        Helper function to maintain order of heap (parent is greater than children)
        index is the LOCATION
        :return: None
        """
        leftChild = 2*position + 1 #set the value of the leftChild of position
        rightChild = 2*position + 2 #set the value of the rightChild of position
        ret = -1 #default ret value
        while(position != -1):
            if(leftChild < self._currentSize):
                if(self._heap[leftChild].ticketID > self._heap[rightChild].ticketID): #check ticketID's for priority
                    if(self._heap[leftChild].ticketID > self._heap[position].ticketID): #
                        self._swap(leftChild, position) #swap the two positions
                        position = leftChild #update the position value
                        leftChild = 2*position + 1 #get the leftChild of position node
                        rightChild = 2*position + 2 #get the rightChild of position node
                elif(self._heap[rightChild].ticketID > self._heap[position].ticketID): #rightChild ticketID is greater than position ticketID
                    self._swap(rightChild, position) #swap the two positions
                    position = rightChild #update position value
                    leftChild = 2*position + 1
                    rightChild = 2*position + 2
                else:
                    position = -1
            else:
                position = -1
        return ret

    #DONE
    def enqueue(self, ticket): #TAKES A MEALTICKET
        """
    Complexity: O(lg(n))
    Valid input: An object of type: MealTicket. Return false
    Description: This method will add a ticket to the queue based on its priority
    Note 1: The priority a ticket is determined by its ID
    Note 2: When adding a node to your heap, remember that every node n, the value
        n must be GREATER THAN OR EQUAL to the values of its children, but your heap
        must also maintain the correct shape (i.e. for any node there can be at most
        two children, and the parent has a greater priority than all subsequent nodes.
    Returns TRUE if enqueue was SUCCESSFUL
        """

        ret = False
        if(type(ticket) == MealTicket and not self.isFull()):
            if self.isEmpty():
                self._heap.append(ticket)
                self._currentSize += 1
                ret = True #just append ticket, don't call heapify because the heap is automatically maintained
            else: #more than 1 value in heap already
                self._heap.append(ticket) #append new ticket
                self._currentSize += 1 #increment size of the prioQueue
                position = self._currentSize - 1 #get the position of the last node
                parent = self._getParent(position) #get the parent of the last node
                while(parent >= 0): #check this case
                    if(self._heap[parent].ticketID < self._heap[position].ticketID): #priorities (ticketID's), need to be checked
                        self._swap(position, parent) #if the above condition is TRUE, we need to swap values
                        position = parent #update position value
                        parent = self._getParent(position) #get the position's parent
                    else:
                        break #the if statement above is FALSE, meaning heap is maintained
                ret = True #update the return value
        return ret


    #DONE- RETURNING FIRST ELEMENT IN HEAP
    def dequeueMax(self):
        """
    Complexity: O(nlg(n)) or LESS
    Description: This method will remove AND return the ticket with the highest
        priority. If the queue is empty, then it will return False
    Return: a boolean value if SUCCESSFUL
        """
        """
        
        ret = False
        if(self.isEmpty() != True): #is NOT EMPTY- do the thing
            newMax = self._heap[0]
            ret = newMax
            self._heap[0] = self._heap[self._currentSize]
            self._currentSize -= 1
            self._heapify(0) #start at index zero (or root) to heapify through everything
        return ret
        """
        if(self.isEmpty()):
            max = False #heap is empty
        elif(self._currentSize == 1): #only one item in the heap
            max = self._heap.pop(0)
            self._currentSize -= 1
            #dont call heapify, it will crash because there is no parent node
        else: #heap IS NOT EMPTY
            max = self._heap.pop(0) #head of the heap, or root should have highest priority
            self._heap.insert(0,self._heap.pop()) #insert last node into root
            self._currentSize -= 1
            #position = self._currentSize - 1
            if(self._heap[0].ticketID < self._heap[self._leftChild(0)].ticketID or self._heap[0].ticketID < self._heap[self._rightChild(0)].ticketID):
                self._heapify(0) #start at index 0 to heapify through ENTIRE HEAP
            #this is what makes it nlogn
        return max

    #DONE
    def peekMax(self):
        """
    Complexity: O(1)
    Description: This method will remove and return the ticket with the highest
        priority (HIGHEST TICKETID) ->should be in first index of heap.
    Returns false if the queue is empty.
        """
        retVal = False
        if(self.isEmpty() != True):
            retVal = self._heap[0] #highest priority
        return retVal

    def isEmpty(self):
        return (self._currentSize == 0) #PrioQueue is Empty

    def isFull(self):
        return (self._currentSize == self._maxSize) #PrioQueue size = max capacity
