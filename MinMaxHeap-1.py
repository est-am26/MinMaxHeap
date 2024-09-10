# "I hereby certify that this program is solely the result of my own work and is in compliance with the Academic 
# Integrity policy of the course syllabus and the academic integrity policy of the CS department.”

# Import the math module to be able to use math functions:
import math 

# Class to represent a node in the min-max heap:
class Node(object):
    
    # Constructor to initialize a node with a key and data:
    def __init__(self, key, data):
        self.key = key
        self.data = data      

# Class to represent a min-max heap data structure:
class minMaxHeap(object):
    
    # Constructor to initialize a min-max heap with the given size:
    def __init__(self, size):
        self.__arr = [None] * (size + 1)
        self.__nElems =  0
        self.__size = size
    
    # This method returns the string representation of the keys of 
    # the elements in the heap:
    def __str__(self):
        # Initializes an empty list, iterates through the keys of the 
        # heap and append them to it:
        string = []
        for k in range(self.__nElems):
            string.append(self.__arr[k].key)
        return str(string)        
    
    # This method returns the number of elements currently stored in the
    # min-max heap:
    def __len__(self):
        return self.__nElems
    
    # This method calculates the level of a node in the min-max heap 
    # based on its index:
    def __level(self, cur):
        return int(math.log2(cur+1))
    
    # This method determines whether the push-down operation should be performed as a min-level 
    # operation or a max-level operation based on the level of the element:    
    def __pushDown(self, cur):
        # Check if the specified index is valid:
        if cur >= 0 and cur < self.__nElems:
            if self.__level(cur) % 2 == 0:
                self.__pushDownMin(cur)
            else:
                self.__pushDownMax(cur)
           
    # This method performs the push-down operation at the specified index in 
    # the min-max heap on elements in the min (even) levels:
    def __pushDownMin(self, cur):    
        # Check if the specified index is valid and if the element has children:
        if self.__arr[cur] is not None and cur <= self.__size // 2:
            smallestChild = cur
                        
            # Get children and grandchildren:
            leftChild = 2 * cur + 1            
            rightChild = leftChild + 1
            leftGrandchild1 = 2 * leftChild + 1
            leftGrandchild2 = leftGrandchild1 + 1
            rightGrandchild1 = 2 * rightChild + 1
            rightGrandchild2 = rightGrandchild1 + 1
            
            # Find the smallest among the current node, its children, and its grandchildren:
            for i in [leftChild, rightChild, leftGrandchild1, leftGrandchild2, rightGrandchild1, rightGrandchild2]:
                if i < self.__nElems and self.__arr[i] is not None and self.__arr[i].key < self.__arr[smallestChild].key:
                    smallestChild = i     
                    
            # Find the parent:         
            parent = (smallestChild - 1) // 2
            
            # If the smallest node is a grandchild, check its relationship with its parent and grandparent, and swap it if necessary:
            if smallestChild >= (2 * leftChild + 1):
                if self.__arr[smallestChild].key < self.__arr[cur].key:                
                    self.__arr[smallestChild], self.__arr[cur] = self.__arr[cur], self.__arr[smallestChild]
                    
                    if self.__arr[smallestChild].key > self.__arr[parent].key:                   
                        self.__arr[smallestChild], self.__arr[parent] = self.__arr[parent], self.__arr[smallestChild]
                                
                    # Perform push-down recursively on the smallest node:
                    self.__pushDown(smallestChild)                     
                    
            else:      
                # If the smallest node is a child and smaller than its father, swap it with the father:
                if self.__arr[smallestChild].key < self.__arr[cur].key:
                    self.__arr[smallestChild], self.__arr[cur] = self.__arr[cur], self.__arr[smallestChild]
                    
    # This method performs the push-down operation at the specified index in 
    # the min-max heap on elements in the max (odd) levels:                    
    def __pushDownMax(self, cur):   
        # Check if the specified index is valid and if the element has children:
        if self.__arr[cur] is not None and cur <= self.__size // 2:
            largestChild = cur   
            
            # Get children and grandchildren:
            leftChild = 2 * cur + 1
            rightChild = leftChild + 1
            leftGrandchild1 = 2 * leftChild + 1
            leftGrandchild2 = leftGrandchild1 + 1
            rightGrandchild1 = 2 * rightChild + 1
            rightGrandchild2 = rightGrandchild1 + 1
            
            # Find the largest among the current node, its children, and its grandchildren:
            for i in [leftChild, rightChild, leftGrandchild1, leftGrandchild2, rightGrandchild1, rightGrandchild2]:
                if i < self.__nElems and self.__arr[i] is not None and self.__arr[i].key > self.__arr[largestChild].key:
                    largestChild = i   
            
            # Find the parent:          
            parent = (largestChild - 1) // 2
             
            # If the largest node is a grandchild, check its relationship with its parent and grandparent, and swap it if necessary:
            if largestChild >= (2 * leftChild + 1):
                if self.__arr[largestChild].key > self.__arr[cur].key:
                    self.__arr[largestChild], self.__arr[cur] = self.__arr[cur], self.__arr[largestChild]
                    
                    if self.__arr[largestChild].key < self.__arr[parent].key:
                        self.__arr[largestChild], self.__arr[parent] = self.__arr[parent], self.__arr[largestChild]                          
                    
                    # Perform push-down recursively on the largest node:    
                    self.__pushDown(largestChild)  
                          
            else: 
                # If the largest node is a child and bigger than its father, swap it with the father:
                if self.__arr[largestChild].key > self.__arr[cur].key:
                    self.__arr[largestChild], self.__arr[cur] = self.__arr[cur], self.__arr[largestChild]    
        
    
    # This method pushes up the element at index 'cur' until the heap property is satisfied:
    def __pushUp(self, cur):
        # Check if the current index is not the root:
        if cur > 0:
            
            # Calculate the parent index:
            parent = (cur - 1) //2
            
            # Check if the current level is a min level
            if self.__level(cur) % 2 == 0:
                
                # If it exists and its greater than its father, swap it:
                if self.__arr[cur] is not None:
                    if self.__arr[cur].key > self.__arr[parent].key:
                        self.__arr[cur], self.__arr[parent] = self.__arr[parent], self.__arr[cur]    
                        
                        # Recursively push up the parent on the max level:
                        self.__pushUpMax(parent)
                       
                    # If it isn't greater, recursively push up on the min level: 
                    else:
                        self.__pushUpMin(cur)
            
            # Otherwise, the current level is on a max level (odd):        
            else:
                # If the current node exists and is smaller than its parent, swap it: 
                if self.__arr[cur] is not None:
                    if self.__arr[cur].key < self.__arr[parent].key:
                        self.__arr[cur], self.__arr[parent] = self.__arr[parent], self.__arr[cur] 
                        
                        # Recursively push up the parent on the min level:
                        self.__pushUpMin(parent)
                       
                    # If it isn't smaller, recursively push up on the min level:  
                    else:
                        self.__pushUpMax(cur)
    
    
    # This method pushes up the element at index 'cur' on the min level until the 
    # heap property is satisfied:              
    def __pushUpMin(self, cur):
        # Calculate the grandparent index:
        parent = (cur - 1) // 2
        grandparent = (parent - 1) // 2
        
        # If there's a grandparent and the current node is smaller than its grandparent, swap it:
        if grandparent >= 0 and self.__arr[cur].key < self.__arr[grandparent].key:
            self.__arr[cur], self.__arr[grandparent] = self.__arr[grandparent], self.__arr[cur] 
            
            # Recursively push up the grandparent on the min level:
            self.__pushUpMin(grandparent)
                    
                    
    # This method pushes up the element at index 'cur' on the max level until the 
    # heap property is satisfied:     
    def __pushUpMax(self, cur):
        # Calculate the grandparent index:
        parent = (cur - 1) // 2
        grandparent = (parent - 1) // 2
        
        # If there's a grandparent and the current node is bigger than its grandparent, swap it:
        if grandparent >= 0 and self.__arr[cur].key > self.__arr[grandparent].key:
            self.__arr[cur], self.__arr[grandparent] = self.__arr[grandparent], self.__arr[cur]
            
            # Recursively push up the grandparent on the max level:
            self.__pushUpMax(grandparent)   
        
    # Inserts a new node with key `k` and data `d` into the min-max heap:
    def insert(self, k, d):
        # Fail if the heap is full:
        if self.__nElems == len(self.__arr): 
            return False 
    
        # Create a new node and insert it into the array:
        self.__arr[self.__nElems] = Node(k, d)
        
        # Increment the number of elements:
        self.__nElems += 1   
        
        # Recursively push up the last element inserted:
        self.__pushUp(self.__nElems-1)
        
        return True    
    
    # This method finds the minimum element on the heap: 
    def findMinimum(self):
        # If the heap is empty, returns None: 
        if self.__nElems == 0:
            return None, None  
        
        # Otherwise, returns the root: 
        else: 
            return self.__arr[0].key, self.__arr[0].data
    
    # This method finds the maximum element on the heap: 
    def findMaximum(self, cur = 0):
        # If the heap is empty, returns None:
        if self.__nElems == 0: return None, None  
        
        # If there's only one element in the heap, return its key and data:
        elif self.__nElems == 1:
            return self.__arr[0].key, self.__arr[0].data
        
        else: 
            # Indeces of the left and right child of the current node:
            leftChild = 1 
            rightChild = 2
            
            # Find which of the children (right or left) is greater:
            if self.__arr[leftChild] is not None:
                largerChild = leftChild
            
            if self.__arr[rightChild] is not None:
                if rightChild < self.__nElems and self.__arr[leftChild].key < self.__arr[rightChild].key:
                    largerChild = rightChild        
            
            # Return the key and data of the larger child:
            return self.__arr[largerChild].key, self.__arr[largerChild].data
    
    # Method to remove the minimum element from the heap:
    def removeMinimum(self):
        # If the heap is empty, returns None: 
        if self.__nElems == 0: return None, None 
        
        # Answer will be key/data pair from the root node:
        root = self.__arr[0]
        
        # Now place the last node in the heap into the root location,
        # and trickle it down:
        self.__arr[0] = self.__arr[self.__nElems-1]
        self.__nElems -= 1
        self.__pushDown(0)
        
        # Keep garbage collector happy:
        self.__arr[self.__nElems] = None
        
        # Return the key and data of the removed root node:
        return root.key, root.data    
     
    # Method to remove the maximum element from the heap:   
    def removeMaximum(self, cur = 0):
        # If the heap is empty, returns None: 
        if self.__nElems == 0: 
            return None, None 
        
        # Store the root node:
        root = self.__arr[0]
        
        # If there's only one element in the heap, remove it and return its key and data:
        if self.__nElems == 1:
            self.__nElems -= 1
            self.__arr[0] = None
            return root.key, root.data            
        
        # Index of the left child of the current node:
        leftChild = 1 
        # Index of the right child of the current node:
        rightChild = 2
        
        # Find which of the children (right or left) is greater:
        largerChild = None
        if leftChild < self.__nElems:
            largerChild = leftChild
            if rightChild < self.__nElems and self.__arr[leftChild].key < self.__arr[rightChild].key:
                largerChild = rightChild
                
        if largerChild is not None:
            largerK, largerD = self.__arr[largerChild].key, self.__arr[largerChild].data
        else:
            return None, None          
        
        # Now place the last node in the heap into the largerChild location,
        # reduce the number of elements and trickle it down to restore the heap property:
        self.__arr[largerChild] = self.__arr[self.__nElems-1]
        self.__nElems -= 1
        self.__pushDown(largerChild)
        
        # Return the key and data of the removed larger child:
        return largerK, largerD
              
                
def main():
    # Create a minMaxHeap instance with an initial capacity of 20:
    MinMaxHeap = minMaxHeap(20)

    # Insert 20 elements:
    MinMaxHeap.insert(10, "d10")
    MinMaxHeap.insert(11, "d11")
    MinMaxHeap.insert(5, "d5")
    MinMaxHeap.insert(13, "d13")
    MinMaxHeap.insert(19, "d19")    
    MinMaxHeap.insert(22, "d22")
    MinMaxHeap.insert(9, "d9")
    MinMaxHeap.insert(8, "d8")
    MinMaxHeap.insert(25, "d25")
    MinMaxHeap.insert(7, "d7")
    MinMaxHeap.insert(2, "d2")
    MinMaxHeap.insert(30, "d30")
    MinMaxHeap.insert(40, "d40")

    # Print the MinMaxHeap after insertion:
    print("\nAfter insertion:")
    print(MinMaxHeap)
    
    # Find the minimum element of MinMaxHeap:
    print("\nThe minimum is:", MinMaxHeap.findMinimum())
    
    # Find the maximum element of MinMaxHeap:
    print("\nThe maximum is:", MinMaxHeap.findMaximum())

    # Remove the minimum element from MinMaxHeap:
    print("\nMinimum element removed:", MinMaxHeap.removeMinimum())

    # Print the MinMaxHeap after removing the minimum:
    print("\nAfter removing the minimum:")
    print(MinMaxHeap)

    # Remove the maximum element from MinMaxHeap: 
    print("\nMaximum element removed:", MinMaxHeap.removeMaximum())
   
    # Print the MinMaxHeap after removing maximum: 
    print("\nAfter removing the maximum:")
    print(MinMaxHeap)
    
    # Find the minimum element of MinMaxHeap after removals:
    print("\nThe minimum is:", MinMaxHeap.findMinimum())
    
    # Find the maximum element of MinMaxHeap after removals:
    print("\nThe maximum is:", MinMaxHeap.findMaximum())    
    
    # Remove the minimum element from MinMaxHeap again:
    print("\nMinimum element removed:", MinMaxHeap.removeMinimum())
 
    # Print MinMaxHeap after removing the minimum again:
    print("\nAfter removing the minimum:")
    print(MinMaxHeap)    
    
    # Remove the maximum element from MinMaxHeap again:
    print("\nMaximum element removed:", MinMaxHeap.removeMaximum())
   
    # Print MinMaxHeap after removing maximum again: 
    print("\nAfter removing the maximum:")
    print(MinMaxHeap)
    
    # Find the minimum element of MinMaxHeap after additional removals:
    print("\nThe minimum is:", MinMaxHeap.findMinimum())
    
    # Find the maximum element of MinMaxHeap after additional removals:
    print("\nThe maximum is:", MinMaxHeap.findMaximum())    
    
if __name__ == "__main__":
    main()
