# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data  
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None 
        
  
    def push(self, new_data):
        newNode = Node(new_data)

        if self.head is None:
            self.head = newNode
            return

        # travel to the end of the linked list
        travellingPointer = self.head

        while travellingPointer.next is not None:
            travellingPointer = travellingPointer.next
         
        # Append new node to the end of linked list
        travellingPointer.next = newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slowPointer = fastPointer = self.head
        while fastPointer is not None and fastPointer.next is not None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        if slowPointer is not None:
            print(slowPointer.data)
        return

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.printMiddle() 
