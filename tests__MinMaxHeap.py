# "I hereby certify that this program is solely the result of my own work and is in compliance with the Academic 
# Integrity policy of the course syllabus and the academic integrity policy of the CS department.”

import pytest
import random
from MinMaxHeapHW import minMaxHeap

# This class represents a simulated version of a MinMaxHeap, 
# mimicking its basic behavior using a list of tuples:
class FakeMinMaxHeap(object):
    # Constructor that initializes a list to store the 'heap' elements, 
    # along with its maximum size and current number of elements:
    def __init__(self, size):
        self.__array = [] 
        self.__size = size
        self.__nElems = 0
        
    # Method to insert a new element into the list:
    def insert(self, key, data):
        # Append the new element to the list and 
        # increment the number of elements:
        self.__array.append((key, data))
        self.__nElems += 1
    
    # Method that returns a string representation of the list: 
    def __str__(self):
        return str(self.__array)
        
    # Method that returns the current number of 
    # elements in the list:
    def __len__(self):
        return self.__nElems
        
    # This method finds and returns the minimum element in the list:
    def findMinimum(self):
        # Return None if the list is empty:
        if self.__nElems == 0:
            return None, None
        
        # Assume the first element as the minimum and get its key:
        minimum = self.__array[0]
        minimumKey = minimum[0]
        
        # Iterate through the remaining elements to 
        # find the minimum:
        for i in self.__array[1:]:
            # Update the minimum element and the minimum 
            # key if a smaller element is found:
            if i[0] < minimumKey:
                minimum = i
                minimumKey = i[0]
        
        # Return the minimum element:             
        return minimum
    
    # This method finds and returns the maximum element in the list:    
    def findMaximum(self):
        # Return None if the list is empty:
        if self.__nElems == 0:
            return None, None
        
        # Assume the first element as the maximum and get its key:
        maximum = self.__array[0]
        maximumKey = maximum[0]
        
        # Iterate through the remaining elements to 
        # find the maximum:        
        for i in self.__array[1:]:
            # Update the maximum element and the maximum 
            # key if a bigger element is found:            
            if i[0] > maximumKey:
                maximum = i
                maximumKey = i[0]
        
        # Return the maximum element:         
        return maximum        
     
    # This method removes and returns the minimum element in the list:    
    def removeMinimum(self):
        # Return None if the list is empty:
        if self.__nElems == 0:
            return None, None
        
        # Assume the first element as the minimum and get its key:
        minimum = self.__array[0]
        minimumKey = minimum[0]
        
        # Iterate through the remaining elements to 
        # find the minimum:         
        for i in self.__array[1:]:
            if i[0] < minimumKey:
                minimum = i
                minimumKey = i[0]
        
        # Remove the minimum:
        self.__array.remove(minimum)
        # Decrease the number elements: 
        self.__nElems -= 1
        
        # Return the minimum element: 
        return minimum             
    
    # This method removes and returns the maximum element in the list:    
    def removeMaximum(self):
        # Return None if the list is empty:
        if self.__nElems == 0:
            return None, None
        
        # Assume the first element as the maximum and get its key:
        maximum = self.__array[0]
        maximumKey = maximum[0]
        
        # Iterate through the remaining elements to 
        # find the maximum:        
        for i in self.__array[1:]:
            if i[0] > maximumKey:
                maximum = i
                maximumKey = i[0]
        
        # Remove the maximum:        
        self.__array.remove(maximum)
        # Decrease the number of elements:
        self.__nElems -= 1
        
        # Return the maximum element:
        return maximum            
        
# Tests:        

# Create empty instances of minMaxHeap and FakeMinMaxHeap
# and tests the removeMinimum() method in both of them:
def test_emptyRemoveMinimum():
    # Create a MinMaxHeap and FakeMinMaxHeap with zero capacity: 
    t = minMaxHeap(0)
    f = FakeMinMaxHeap(0)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with small capacity: 
    trueEmptySmallCapacity = minMaxHeap(3)
    fakeEmptySmallCapacity = FakeMinMaxHeap(3)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with big capacity: 
    trueEmptyBigCapacity = minMaxHeap(100)
    fakeEmptyBigCapacity = FakeMinMaxHeap(100)   
    
    # Check that in all cases it's removing the minimum correctly:
    assert t.removeMinimum() == f.removeMinimum()
    assert trueEmptySmallCapacity.removeMinimum() == fakeEmptySmallCapacity.removeMinimum()
    assert trueEmptyBigCapacity.removeMinimum() == fakeEmptyBigCapacity.removeMinimum()
    

# Create empty instances of minMaxHeap and FakeMinMaxHeap
# and tests the removeMaximum() method in both of them:
def test_emptyRemoveMaximum():
    # Create a MinMaxHeap and FakeMinMaxHeap with zero capacity: 
    t = minMaxHeap(0)
    f = FakeMinMaxHeap(0)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with small capacity: 
    trueEmptySmallCapacity = minMaxHeap(3)
    fakeEmptySmallCapacity = FakeMinMaxHeap(3)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with big capacity:
    trueEmptyBigCapacity = minMaxHeap(100)
    fakeEmptyBigCapacity = FakeMinMaxHeap(100)   
    
    # Check that in all cases it's removing the maximum correctly:
    assert t.removeMaximum() == f.removeMaximum()
    assert trueEmptySmallCapacity.removeMaximum() == fakeEmptySmallCapacity.removeMaximum()
    assert trueEmptyBigCapacity.removeMaximum() == fakeEmptyBigCapacity.removeMaximum()    
    
    
# Create empty instances of minMaxHeap and FakeMinMaxHeap
# and tests the findMinimum() method in both of them:    
def test_emptyFindMinimum():
    # Create a MinMaxHeap and FakeMinMaxHeap with zero capacity: 
    t = minMaxHeap(0)
    f = FakeMinMaxHeap(0)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with small capacity:
    trueEmptySmallCapacity = minMaxHeap(3)
    fakeEmptySmallCapacity = FakeMinMaxHeap(3)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with big capacity:
    trueEmptyBigCapacity = minMaxHeap(100)
    fakeEmptyBigCapacity = FakeMinMaxHeap(100)   
    
    # Check that in all cases it's finding the minimum correctly:
    assert t.findMinimum() == f.findMinimum()
    assert trueEmptySmallCapacity.findMinimum() == fakeEmptySmallCapacity.findMinimum()
    assert trueEmptyBigCapacity.findMinimum() == fakeEmptyBigCapacity.findMinimum()    


# Create empty instances of minMaxHeap and FakeMinMaxHeap
# and tests the findMaximum() method in both of them:  
def test_emptyFindMaximum():
    # Create a MinMaxHeap and FakeMinMaxHeap with zero capacity: 
    t = minMaxHeap(0)
    f = FakeMinMaxHeap(0)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with small capacity:
    trueEmptySmallCapacity = minMaxHeap(3)
    fakeEmptySmallCapacity = FakeMinMaxHeap(3)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with big capacity:
    trueEmptyBigCapacity = minMaxHeap(100)
    fakeEmptyBigCapacity = FakeMinMaxHeap(100)   
    
    # Check that in all cases it's finding the maximum correctly:
    assert t.findMaximum() == f.findMaximum()
    assert trueEmptySmallCapacity.findMaximum() == fakeEmptySmallCapacity.findMaximum()
    assert trueEmptyBigCapacity.findMaximum() == fakeEmptyBigCapacity.findMaximum()       


# Create empty instances of minMaxHeap and FakeMinMaxHeap
# and test if both of them have the same legth:   
def test_emptyLen():
    # Create a MinMaxHeap and FakeMinMaxHeap with zero capacity: 
    t = minMaxHeap(0)
    f = FakeMinMaxHeap(0)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with small capacity:
    trueEmptySmallCapacity = minMaxHeap(3)
    fakeEmptySmallCapacity = FakeMinMaxHeap(3)
    
    # Create a MinMaxHeap and FakeMinMaxHeap with big capacity:
    trueEmptyBigCapacity = minMaxHeap(100)
    fakeEmptyBigCapacity = FakeMinMaxHeap(100)   
    
    # Check that in all cases both have the same length:
    assert len(t) == len(f)
    assert len(trueEmptySmallCapacity) == len(fakeEmptySmallCapacity)
    assert len(trueEmptyBigCapacity) == len(fakeEmptyBigCapacity)       


# Create one-element instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMinimum() method works:       
def test_OneElementRemoveMinimum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of one and insert one element: 
    t = minMaxHeap(1)
    t.insert(13, "d13")
    f = FakeMinMaxHeap(1)
    f.insert(13, "d13")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert one element:     
    trueOneElementSmallCapacity = minMaxHeap(3)
    trueOneElementSmallCapacity.insert(42, "d42")
    fakeOneElementSmallCapacity = FakeMinMaxHeap(3)
    fakeOneElementSmallCapacity.insert(42, "d42")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert one element:     
    trueOneElementBigCapacity = minMaxHeap(100)
    trueOneElementBigCapacity.insert(59, "d59")
    fakeOneElementBigCapacity = FakeMinMaxHeap(100)   
    fakeOneElementBigCapacity.insert(59, "d59")
    
    # Check that in all cases it's removing the minimum correctly:
    assert t.removeMinimum() == f.removeMinimum()
    assert trueOneElementSmallCapacity.removeMinimum() == fakeOneElementSmallCapacity.removeMinimum()
    assert trueOneElementBigCapacity.removeMinimum() == fakeOneElementBigCapacity.removeMinimum()


# Create one-element instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMaximum() method works:         
def test_OneElementRemoveMaximum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of one and insert one element:     
    t = minMaxHeap(1)
    t.insert(45, "d45")
    f = FakeMinMaxHeap(1)
    f.insert(45, "d45")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert one element:         
    trueOneElementSmallCapacity = minMaxHeap(3)
    trueOneElementSmallCapacity.insert(26, "d26")
    fakeOneElementSmallCapacity = FakeMinMaxHeap(3)
    fakeOneElementSmallCapacity.insert(26, "d26")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert one element:         
    trueOneElementBigCapacity = minMaxHeap(100)
    trueOneElementBigCapacity.insert(36, "d36")
    fakeOneElementBigCapacity = FakeMinMaxHeap(100)   
    fakeOneElementBigCapacity.insert(36, "d36") 
    
    # Check that in all cases it's removing the maximum correctly:
    assert t.removeMaximum() == f.removeMaximum()
    assert trueOneElementSmallCapacity.removeMaximum() == fakeOneElementSmallCapacity.removeMaximum()
    assert trueOneElementBigCapacity.removeMaximum() == fakeOneElementBigCapacity.removeMaximum()    


# Create one-element instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMinimum() method works:         
def test_OneElementFindMinimum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of one and insert one element:         
    t = minMaxHeap(1)
    t.insert(64, "d64")
    f = FakeMinMaxHeap(1)
    f.insert(64, "d64")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert one element:             
    trueOneElementSmallCapacity = minMaxHeap(3)
    trueOneElementSmallCapacity.insert(30, "d30")
    fakeOneElementSmallCapacity = FakeMinMaxHeap(3)
    fakeOneElementSmallCapacity.insert(30, "d30")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert one element:       
    trueOneElementBigCapacity = minMaxHeap(100)
    trueOneElementBigCapacity.insert(2, "d2")
    fakeOneElementBigCapacity = FakeMinMaxHeap(100)   
    fakeOneElementBigCapacity.insert(2, "d2") 
     
    # Check that in all cases it's finding the minimum correctly:
    assert t.findMinimum() == f.findMinimum()
    assert trueOneElementSmallCapacity.findMinimum() == fakeOneElementSmallCapacity.findMinimum()
    assert trueOneElementBigCapacity.findMinimum() == fakeOneElementBigCapacity.findMinimum()    


# Create one-element instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMaximum() method works:         
def test_OneElementFindMaximum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of one and insert one element:      
    t = minMaxHeap(1)
    t.insert(10, "d10")
    f = FakeMinMaxHeap(1)
    f.insert(10, "d10")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert one element:         
    trueOneElementSmallCapacity = minMaxHeap(3)
    trueOneElementSmallCapacity.insert(49, "d49")
    fakeOneElementSmallCapacity = FakeMinMaxHeap(3)
    fakeOneElementSmallCapacity.insert(49, "d49")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert one element:         
    trueOneElementBigCapacity = minMaxHeap(100)
    trueOneElementBigCapacity.insert(97, "d97")
    fakeOneElementBigCapacity = FakeMinMaxHeap(100)   
    fakeOneElementBigCapacity.insert(97, "d97") 
      
    # Check that in all cases it's finding the maximum correctly:
    assert t.findMaximum() == f.findMaximum()
    assert trueOneElementSmallCapacity.findMaximum() == fakeOneElementSmallCapacity.findMaximum()
    assert trueOneElementBigCapacity.findMaximum() == fakeOneElementBigCapacity.findMaximum()       
    

# Create one-element instances of minMaxHeap and FakeMinMaxHeap
# and test if both of them have the same legth:       
def test_OneElementLen():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of one and insert one element:       
    t = minMaxHeap(1)
    t.insert(63, "d63")
    f = FakeMinMaxHeap(1)
    f.insert(63, "d63")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert one element:             
    trueOneElementSmallCapacity = minMaxHeap(3)
    trueOneElementSmallCapacity.insert(14, "d14")
    fakeOneElementSmallCapacity = FakeMinMaxHeap(3)
    fakeOneElementSmallCapacity.insert(14, "d14")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert one element:     
    trueOneElementBigCapacity = minMaxHeap(100)
    trueOneElementBigCapacity.insert(72, "d72")
    fakeOneElementBigCapacity = FakeMinMaxHeap(100)   
    fakeOneElementBigCapacity.insert(72, "d72") 
     
    # Check that in all cases both have the same length:
    assert len(t) == len(f)
    assert len(trueOneElementSmallCapacity) == len(fakeOneElementSmallCapacity)
    assert len(trueOneElementBigCapacity) == len(fakeOneElementBigCapacity)    
    
    
# Create two-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMinimum() method works:       
def test_TwoElementsRemoveMinimum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert two elements:      
    t = minMaxHeap(2)
    t.insert(22, "d22")
    t.insert(74, "d74")
    f = FakeMinMaxHeap(2)
    f.insert(22, "d22")
    f.insert(74, "d74")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert two elements:         
    trueTwoElementsSmallCapacity = minMaxHeap(3)
    trueTwoElementsSmallCapacity.insert(76, "d76")
    trueTwoElementsSmallCapacity.insert(81, "d81")
    fakeTwoElementsSmallCapacity = FakeMinMaxHeap(3)
    fakeTwoElementsSmallCapacity.insert(76, "d76")
    fakeTwoElementsSmallCapacity.insert(81, "d81")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert two elements:       
    trueTwoElementsBigCapacity = minMaxHeap(100)
    trueTwoElementsBigCapacity.insert(50, "d50")
    trueTwoElementsBigCapacity.insert(95, "d95")
    fakeTwoElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeTwoElementsBigCapacity.insert(50, "d50")
    fakeTwoElementsBigCapacity.insert(95, "d95")
    
    # Check that in all cases it's finding the minimum correctly:
    assert t.removeMinimum() == f.removeMinimum()
    assert trueTwoElementsSmallCapacity.removeMinimum() == fakeTwoElementsSmallCapacity.removeMinimum()
    assert trueTwoElementsBigCapacity.removeMinimum() == fakeTwoElementsBigCapacity.removeMinimum()

# Create two-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMaximum() method works:       
def test_TwoElementsRemoveMaximum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert two elements:      
    t = minMaxHeap(2)
    t.insert(33, "d33")
    t.insert(28, "d28")
    f = FakeMinMaxHeap(2)
    f.insert(33, "d33")
    f.insert(28, "d28")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert two elements:             
    trueTwoElementsSmallCapacity = minMaxHeap(3)
    trueTwoElementsSmallCapacity.insert(67, "d67")
    trueTwoElementsSmallCapacity.insert(90, "d90")
    fakeTwoElementsSmallCapacity = FakeMinMaxHeap(3)
    fakeTwoElementsSmallCapacity.insert(67, "d67")
    fakeTwoElementsSmallCapacity.insert(90, "d90")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert two elements:           
    trueTwoElementsBigCapacity = minMaxHeap(100)
    trueTwoElementsBigCapacity.insert(62, "d62")
    trueTwoElementsBigCapacity.insert(1, "d1")
    fakeTwoElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeTwoElementsBigCapacity.insert(62, "d62")
    fakeTwoElementsBigCapacity.insert(1, "d1")
    
    # Check that in all cases it's removing the maximum correctly:
    assert t.removeMaximum() == f.removeMaximum()
    assert trueTwoElementsSmallCapacity.removeMaximum() == fakeTwoElementsSmallCapacity.removeMaximum()
    assert trueTwoElementsBigCapacity.removeMaximum() == fakeTwoElementsBigCapacity.removeMaximum()    

# Create two-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMinimum() method works:      
def test_TwoElementsFindMinimum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert two elements:       
    t = minMaxHeap(2)
    t.insert(26, "d26")
    t.insert(70, "d70")
    f = FakeMinMaxHeap(2)
    f.insert(26, "d26")
    f.insert(70, "d70")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert two elements:      
    trueTwoElementsSmallCapacity = minMaxHeap(3)
    trueTwoElementsSmallCapacity.insert(39, "d39")
    trueTwoElementsSmallCapacity.insert(19, "d19")
    fakeTwoElementsSmallCapacity = FakeMinMaxHeap(3)
    fakeTwoElementsSmallCapacity.insert(39, "d39")
    fakeTwoElementsSmallCapacity.insert(19, "d19")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert two elements:         
    trueTwoElementsBigCapacity = minMaxHeap(100)
    trueTwoElementsBigCapacity.insert(100, "d100")
    trueTwoElementsBigCapacity.insert(78, "d78")
    fakeTwoElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeTwoElementsBigCapacity.insert(100, "d100")
    fakeTwoElementsBigCapacity.insert(78, "d78")
     
    # Check that in all cases it's finding the minimum correctly:
    assert t.findMinimum() == f.findMinimum()
    assert trueTwoElementsSmallCapacity.findMinimum() == fakeTwoElementsSmallCapacity.findMinimum()
    assert trueTwoElementsBigCapacity.findMinimum() == fakeTwoElementsBigCapacity.findMinimum()    


# Create two-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMaximum() method works:      
def test_TwoElementsFindMaximum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert two elements:       
    t = minMaxHeap(2)
    t.insert(32, "d32")
    t.insert(50, "d50")
    f = FakeMinMaxHeap(2)
    f.insert(32, "d32")
    f.insert(50, "d50")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert two elements:     
    trueTwoElementsSmallCapacity = minMaxHeap(3)
    trueTwoElementsSmallCapacity.insert(77, "d77")
    trueTwoElementsSmallCapacity.insert(84, "d84")
    fakeTwoElementsSmallCapacity = FakeMinMaxHeap(3)
    fakeTwoElementsSmallCapacity.insert(77, "d77")
    fakeTwoElementsSmallCapacity.insert(84, "d84")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert two elements:          
    trueTwoElementsBigCapacity = minMaxHeap(100)
    trueTwoElementsBigCapacity.insert(99, "d99")
    trueTwoElementsBigCapacity.insert(37, "d37")
    fakeTwoElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeTwoElementsBigCapacity.insert(99, "d99")
    fakeTwoElementsBigCapacity.insert(37, "d37")
      
    # Check that in all cases it's finding the maximum correctly:
    assert t.findMaximum() == f.findMaximum()
    assert trueTwoElementsSmallCapacity.findMaximum() == fakeTwoElementsSmallCapacity.findMaximum()
    assert trueTwoElementsBigCapacity.findMaximum() == fakeTwoElementsBigCapacity.findMaximum()       


# Create two-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if both of them have the same legth:      
def test_TwoElementsLen():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert two elements:      
    t = minMaxHeap(2)
    t.insert(42, "d42")
    t.insert(35, "d35")
    f = FakeMinMaxHeap(2)
    f.insert(42, "d42")
    f.insert(35, "d35")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert two elements:       
    trueTwoElementsSmallCapacity = minMaxHeap(3)
    trueTwoElementsSmallCapacity.insert(49, "d49")
    trueTwoElementsSmallCapacity.insert(27, "d27")
    fakeTwoElementsSmallCapacity = FakeMinMaxHeap(3)
    fakeTwoElementsSmallCapacity.insert(49, "d49")
    fakeTwoElementsSmallCapacity.insert(27, "d27")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert two elements:              
    trueTwoElementsBigCapacity = minMaxHeap(100)
    trueTwoElementsBigCapacity.insert(50, "d50")
    trueTwoElementsBigCapacity.insert(99, "d99")
    fakeTwoElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeTwoElementsBigCapacity.insert(50, "d50")
    fakeTwoElementsBigCapacity.insert(99, "d99")
    
    # Check that in all cases both have the same length: 
    assert len(t) == len(f)
    assert len(trueTwoElementsSmallCapacity) == len(fakeTwoElementsSmallCapacity)
    assert len(trueTwoElementsBigCapacity) == len(fakeTwoElementsBigCapacity)    


# Create three-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMinimum() method works:          
def test_ThreeElementsRemoveMinimum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert three elements:        
    t = minMaxHeap(3)
    t.insert(87, "d87")
    t.insert(66, "d66")
    t.insert(53, "d53")
    f = FakeMinMaxHeap(3)
    f.insert(87, "d87")
    f.insert(66, "d66")
    f.insert(53, "d53")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert three elements:    
    trueThreeElementsSmallCapacity = minMaxHeap(5)
    trueThreeElementsSmallCapacity.insert(72, "d72")
    trueThreeElementsSmallCapacity.insert(12, "d12")
    trueThreeElementsSmallCapacity.insert(43, "d43")
    fakeThreeElementsSmallCapacity = FakeMinMaxHeap(5)
    fakeThreeElementsSmallCapacity.insert(72, "d72")
    fakeThreeElementsSmallCapacity.insert(12, "d12")
    fakeThreeElementsSmallCapacity.insert(43, "d43")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert three elements:                
    trueThreeElementsBigCapacity = minMaxHeap(100)
    trueThreeElementsBigCapacity.insert(64, "d64")
    trueThreeElementsBigCapacity.insert(80, "d80")
    trueThreeElementsBigCapacity.insert(134, "d134")
    fakeThreeElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeThreeElementsBigCapacity.insert(64, "d64")
    fakeThreeElementsBigCapacity.insert(80, "d80")
    fakeThreeElementsBigCapacity.insert(134, "d134")
    
    # Check that in all cases it's removing the minimum correctly:
    assert t.removeMinimum() == f.removeMinimum()
    assert trueThreeElementsSmallCapacity.removeMinimum() == fakeThreeElementsSmallCapacity.removeMinimum()
    assert trueThreeElementsBigCapacity.removeMinimum() == fakeThreeElementsBigCapacity.removeMinimum()


# Create three-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMaximum() method works:  
def test_ThreeElementsRemoveMaximum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert three elements:       
    t = minMaxHeap(3)
    t.insert(98, "d98")
    t.insert(7, "d7")
    t.insert(32, "d32")
    f = FakeMinMaxHeap(3)
    f.insert(98, "d98")
    f.insert(7, "d7")
    f.insert(32, "d32")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert three elements:        
    trueThreeElementsSmallCapacity = minMaxHeap(5)
    trueThreeElementsSmallCapacity.insert(47, "d47")
    trueThreeElementsSmallCapacity.insert(9, "d9")
    trueThreeElementsSmallCapacity.insert(120, "d120")
    fakeThreeElementsSmallCapacity = FakeMinMaxHeap(5)
    fakeThreeElementsSmallCapacity.insert(47, "d47")
    fakeThreeElementsSmallCapacity.insert(9, "d9")
    fakeThreeElementsSmallCapacity.insert(120, "d120")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert three elements:      
    trueThreeElementsBigCapacity = minMaxHeap(100)
    trueThreeElementsBigCapacity.insert(85, "d85")
    trueThreeElementsBigCapacity.insert(66, "d66")
    trueThreeElementsBigCapacity.insert(25, "d25")
    fakeThreeElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeThreeElementsBigCapacity.insert(85, "d85")
    fakeThreeElementsBigCapacity.insert(66, "d66")
    fakeThreeElementsBigCapacity.insert(25, "d25")
    
    # Check that in all cases it's removing the maximum correctly:  
    assert t.removeMaximum() == f.removeMaximum()
    assert trueThreeElementsSmallCapacity.removeMaximum() == fakeThreeElementsSmallCapacity.removeMaximum()
    assert trueThreeElementsBigCapacity.removeMaximum() == fakeThreeElementsBigCapacity.removeMaximum()    


# Create three-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMinimum() method works:
def test_ThreeElementsFindMinimum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert three elements:       
    t = minMaxHeap(3)
    t.insert(96, "d96")
    t.insert(38, "d66")
    t.insert(114, "d53")
    f = FakeMinMaxHeap(3)
    f.insert(96, "d96")
    f.insert(38, "d66")
    f.insert(114, "d53")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert three elements:      
    trueThreeElementsSmallCapacity = minMaxHeap(5)
    trueThreeElementsSmallCapacity.insert(4, "d4")
    trueThreeElementsSmallCapacity.insert(17, "d17")
    trueThreeElementsSmallCapacity.insert(23, "d23")
    fakeThreeElementsSmallCapacity = FakeMinMaxHeap(5)
    fakeThreeElementsSmallCapacity.insert(4, "d4")
    fakeThreeElementsSmallCapacity.insert(17, "d17")
    fakeThreeElementsSmallCapacity.insert(23, "d23")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert three elements:          
    trueThreeElementsBigCapacity = minMaxHeap(100)
    trueThreeElementsBigCapacity.insert(2, "d2")
    trueThreeElementsBigCapacity.insert(43, "d43")
    trueThreeElementsBigCapacity.insert(150, "d150")
    fakeThreeElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeThreeElementsBigCapacity.insert(2, "d2")
    fakeThreeElementsBigCapacity.insert(43, "d43")
    fakeThreeElementsBigCapacity.insert(150, "d150")
    
    # Check that in all cases it's finding the minimum correctly:  
    assert t.findMinimum() == f.findMinimum()
    assert trueThreeElementsSmallCapacity.findMinimum() == fakeThreeElementsSmallCapacity.findMinimum()
    assert trueThreeElementsBigCapacity.findMinimum() == fakeThreeElementsBigCapacity.findMinimum()    

    
# Create three-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMaximum() method works:    
def test_ThreeElementsFindMaximum():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert three elements:        
    t = minMaxHeap(3)
    t.insert(14, "d14")
    t.insert(56, "d56")
    t.insert(98, "d98")
    f = FakeMinMaxHeap(3)
    f.insert(14, "d14")
    f.insert(56, "d56")
    f.insert(98, "d98")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert three elements:    
    trueThreeElementsSmallCapacity = minMaxHeap(5)
    trueThreeElementsSmallCapacity.insert(32, "d32")
    trueThreeElementsSmallCapacity.insert(78, "d78")
    trueThreeElementsSmallCapacity.insert(54, "d54")
    fakeThreeElementsSmallCapacity = FakeMinMaxHeap(5)
    fakeThreeElementsSmallCapacity.insert(32, "d32")
    fakeThreeElementsSmallCapacity.insert(78, "d78")
    fakeThreeElementsSmallCapacity.insert(54, "d54")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert three elements:         
    trueThreeElementsBigCapacity = minMaxHeap(100)
    trueThreeElementsBigCapacity.insert(43, "d43")
    trueThreeElementsBigCapacity.insert(12, "d12")
    trueThreeElementsBigCapacity.insert(26, "d26")
    fakeThreeElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeThreeElementsBigCapacity.insert(43, "d43")
    fakeThreeElementsBigCapacity.insert(12, "d12")
    fakeThreeElementsBigCapacity.insert(26, "d26")
      
    # Check that in all cases it's finding the minimum correctly: 
    assert t.findMaximum() == f.findMaximum()
    assert trueThreeElementsSmallCapacity.findMaximum() == fakeThreeElementsSmallCapacity.findMaximum()
    assert trueThreeElementsBigCapacity.findMaximum() == fakeThreeElementsBigCapacity.findMaximum()       
    

# Create three-elements instances of minMaxHeap and FakeMinMaxHeap
# and test if both of them have the same legth: 
def test_ThreeElementsLen():
    # Create a MinMaxHeap and FakeMinMaxHeap with a capacity 
    # of two and insert three elements:          
    t = minMaxHeap(3)
    t.insert(43, "d43")
    t.insert(57, "d57")
    t.insert(93, "d93")
    f = FakeMinMaxHeap(3)
    f.insert(43, "d43")
    f.insert(57, "d57")
    f.insert(93, "d93")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a small capacity 
    # and insert three elements:        
    trueThreeElementsSmallCapacity = minMaxHeap(5)
    trueThreeElementsSmallCapacity.insert(14, "d14")
    trueThreeElementsSmallCapacity.insert(11, "d11")
    trueThreeElementsSmallCapacity.insert(15, "d15")
    fakeThreeElementsSmallCapacity = FakeMinMaxHeap(5)
    fakeThreeElementsSmallCapacity.insert(14, "d14")
    fakeThreeElementsSmallCapacity.insert(11, "d11")
    fakeThreeElementsSmallCapacity.insert(15, "d15")
    
    # Create a MinMaxHeap and FakeMinMaxHeap with a big capacity 
    # and insert three elements:           
    trueThreeElementsBigCapacity = minMaxHeap(100)
    trueThreeElementsBigCapacity.insert(10, "d10")
    trueThreeElementsBigCapacity.insert(22, "d22")
    trueThreeElementsBigCapacity.insert(56, "d56")
    fakeThreeElementsBigCapacity = FakeMinMaxHeap(100)   
    fakeThreeElementsBigCapacity.insert(10, "d10")
    fakeThreeElementsBigCapacity.insert(22, "d22")
    fakeThreeElementsBigCapacity.insert(56, "d56")
     
    # Check that in all cases both have the same length:
    assert len(t) == len(f)
    assert len(trueThreeElementsSmallCapacity) == len(fakeThreeElementsSmallCapacity)
    assert len(trueThreeElementsBigCapacity) == len(fakeThreeElementsBigCapacity) 


# Create regular length instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMinimum() method works:     
def test_RegularLengthRemoveMinimum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 100:
    trueRegularLength = minMaxHeap(100)
    fakeRegularLength = FakeMinMaxHeap(100)   
    
    # Insert random elements into both heaps:
    for k in range(55):
        d = random.randint(1, 100)
        trueRegularLength.insert(d, str(d))
        fakeRegularLength.insert(d, str(d))    
        
    # Check that it's removing the minimum correctly:
    assert trueRegularLength.removeMinimum() == fakeRegularLength.removeMinimum()


# Create regular length instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMaximum() method works:         
def test_RegularLengthRemoveMaximum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 100:
    trueRegularLength = minMaxHeap(100)
    fakeRegularLength = FakeMinMaxHeap(100)   
    
    # Insert random elements into both heaps:
    for k in range(55):
        d = random.randint(1, 100)
        trueRegularLength.insert(d, str(d))
        fakeRegularLength.insert(d, str(d))   
    
    # Check that it's removing the maximum correctly:    
    assert trueRegularLength.removeMaximum() == fakeRegularLength.removeMaximum()  

    
# Create regular length instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMinimum() method works:           
def test_RegularLengthFindMinimum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 100:
    trueRegularLength = minMaxHeap(100)
    fakeRegularLength = FakeMinMaxHeap(100) 
    
    # Insert random elements into both heaps:
    for k in range(55):
        d = random.randint(1, 100)
        trueRegularLength.insert(d, str(d))
        fakeRegularLength.insert(d, str(d))      

    # Check that it's finding the minimum correctly:    
    assert trueRegularLength.findMinimum() == fakeRegularLength.findMinimum()   
    

# Create regular length instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMaximum() method works:      
def test_RegularLengthFindMaximum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 100:
    trueRegularLength = minMaxHeap(100)
    fakeRegularLength = FakeMinMaxHeap(100) 
    
    # Insert random elements into both heaps:
    for k in range(55):
        d = random.randint(1, 100)
        trueRegularLength.insert(d, str(d))
        fakeRegularLength.insert(d, str(d))     
    
    # Check that it's finding the maximum correctly:      
    assert trueRegularLength.findMaximum() == fakeRegularLength.findMaximum()  
    

# Create regular length instances of minMaxHeap and FakeMinMaxHeap
# and test if both have the same number of elements:      
def test_RegularLengthLen():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 100:
    trueRegularLength = minMaxHeap(100)
    fakeRegularLength = FakeMinMaxHeap(100)   
    
    # Insert random elements into both heaps:
    for k in range(55):
        d = random.randint(1, 100)
        trueRegularLength.insert(d, str(d))
        fakeRegularLength.insert(d, str(d))  
    
    # Check that both have the same length:      
    assert len(trueRegularLength) == len(fakeRegularLength) 


# Create very big length instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMinimum() method works:       
def test_VeryBigLengthRemoveMinimum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 5000:
    trueVeryBigLength = minMaxHeap(5000)
    fakeVeryBigLength = FakeMinMaxHeap(5000)  
    
    # Insert random elements into both heaps:
    for k in range(5000):
        d = random.randint(1, 10000)
        trueVeryBigLength.insert(d, str(d))
        fakeVeryBigLength.insert(d, str(d))     
    
    # Check that it's removing the minimum correctly:   
    assert trueVeryBigLength.removeMinimum() == fakeVeryBigLength.removeMinimum()


# Create very big length instances of minMaxHeap and FakeMinMaxHeap
# and test if the removeMaximum() method works:      
def test_VeryBigLengthRemoveMaximum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 5000:
    trueVeryBigLength = minMaxHeap(5000)
    fakeVeryBigLength = FakeMinMaxHeap(5000)   
    
    # Insert random elements into both heaps:
    for k in range(5000):
        d = random.randint(1, 10000)
        trueVeryBigLength.insert(d, str(d))
        fakeVeryBigLength.insert(d, str(d))   
    
    # Check that it's removing the maximum correctly:     
    assert trueVeryBigLength.removeMaximum() == fakeVeryBigLength.removeMaximum()    


# Create very big length instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMinimum() method works:      
def test_VeryBigLengthFindMinimum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 5000:
    trueVeryBigLength = minMaxHeap(5000)
    fakeVeryBigLength = FakeMinMaxHeap(5000)   
    
    # Insert random elements into both heaps:
    for k in range(5000):
        d = random.randint(1, 10000)
        trueVeryBigLength.insert(d, str(d))
        fakeVeryBigLength.insert(d, str(d))      
    
    # Check that it's finding the minimum correctly: 
    assert trueVeryBigLength.findMinimum() == fakeVeryBigLength.findMinimum()    

    
# Create very big length instances of minMaxHeap and FakeMinMaxHeap
# and test if the findMaximum() method works:         
def test_VeryBigLengthFindMaximum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 5000:
    trueVeryBigLength = minMaxHeap(5000)
    fakeVeryBigLength = FakeMinMaxHeap(5000)   
    
    # Insert random elements into both heaps:
    for k in range(5000):
        d = random.randint(1, 100000)
        trueVeryBigLength.insert(d, str(d))
        fakeVeryBigLength.insert(d, str(d))     
    
    # Check that it's finding the maximum correctly:     
    assert trueVeryBigLength.findMaximum() == fakeVeryBigLength.findMaximum()       

    
# Create very big length instances of minMaxHeap and FakeMinMaxHeap
# and test if both have the same length:          
def test_VeryBigLengthLen():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 5000:
    trueVeryBigLength = minMaxHeap(5000)
    fakeVeryBigLength = FakeMinMaxHeap(5000)  
    
    # Insert random elements into both heaps:
    for k in range(5000):
        d = random.randint(1, 10000)
        trueVeryBigLength.insert(d, str(d))
        fakeVeryBigLength.insert(d, str(d))  
    
    # Check if both have the same length:         
    assert len(trueVeryBigLength) == len(fakeVeryBigLength) 


# Create very big length instances of minMaxHeap and FakeMinMaxHeap 
# with the same single element repeated and test if the removeMinimum() method works:      
def test_AllSameElementsRemoveMinimum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 5000:
    trueAllSameElements = minMaxHeap(5000)
    fakeAllSameElements = FakeMinMaxHeap(5000)   
    
    # Insert the same element 5000 times:
    for k in range(5000):
        trueAllSameElements.insert(24, str(24))
        fakeAllSameElements.insert(24, str(24))     
    
    # Check if it's removing the minimum correctly:   
    assert trueAllSameElements.removeMinimum() == fakeAllSameElements.removeMinimum()


# Create very big length instances of minMaxHeap and FakeMinMaxHeap 
# with the same single element repeated and test if the removeMaximum() method works:        
def test_AllSameElementsRemoveMaximum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 5000:
    trueAllSameElements = minMaxHeap(5000)
    fakeAllSameElements= FakeMinMaxHeap(5000)   
    
    # Insert the same element 5000 times:
    for k in range(5000):
        trueAllSameElements.insert(33, str(33))
        fakeAllSameElements.insert(33, str(33))   
    
    # Check if it's removing the maximum correctly:     
    assert trueAllSameElements.removeMaximum() == fakeAllSameElements.removeMaximum()

    
# Create very big length instances of minMaxHeap and FakeMinMaxHeap 
# with the same single element repeated and test if the findMinimum() method works:       
def test_AllSameElementsFindMinimum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 5000:
    trueAllSameElements = minMaxHeap(5000)
    fakeAllSameElements = FakeMinMaxHeap(5000)   
    
    # Insert the same element 5000 times:
    for k in range(5000):
        trueAllSameElements.insert(10, str(10))
        fakeAllSameElements.insert(10, str(10))      
    
    # Check if it's finding the minimum correctly: 
    assert trueAllSameElements.findMinimum() == fakeAllSameElements.findMinimum()


# Create very big length instances of minMaxHeap and FakeMinMaxHeap 
# with the same single element repeated and test if the findMaximum() method works:   
def test_AllSameElementsFindMaximum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 5000:
    trueAllSameElements = minMaxHeap(5000)
    fakeAllSameElements = FakeMinMaxHeap(5000)   
    
    # Insert the same element 5000 times:
    for k in range(5000):
        trueAllSameElements.insert(26, str(26))
        fakeAllSameElements.insert(26, str(26))     
    
    # Check if it's finding the maximum correctly:     
    assert trueAllSameElements.findMaximum() == fakeAllSameElements.findMaximum()     
    
    
# Create very big length instances of minMaxHeap and FakeMinMaxHeap 
# with the same single element repeated and test if both have the same length:       
def test_AllSameElementsLen():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a length of 5000:
    trueAllSameElements = minMaxHeap(5000)
    fakeAllSameElements = FakeMinMaxHeap(5000)   
    
    # Insert the same element 5000 times:
    for k in range(5000):
        trueAllSameElements.insert(54, str(54))
        fakeAllSameElements.insert(54, str(54))  
    
    # Check if both have the same length:      
    assert len(trueAllSameElements) == len(fakeAllSameElements) 


# Create very big length instances of minMaxHeap and FakeMinMaxHeap with random
# elements and some elements that are gonna be repeated for sure and test if the 
# removeMinimum() method works:    
def test_SomeSameElementsRemoveMinimum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 35000:
    trueSomeSameElements = minMaxHeap(35000)
    fakeSomeSameElements = FakeMinMaxHeap(35000)
    
    # Insert a random element and two identical 
    # elements every single time through the loop:
    for k in range(10000):
        d = random.randint(1, 10000)
        trueSomeSameElements.insert(d, str(d))
        fakeSomeSameElements.insert(d, str(d))
        trueSomeSameElements.insert(13, str(13))
        trueSomeSameElements.insert(36, str(36))       
        fakeSomeSameElements.insert(13, str(13))
        fakeSomeSameElements.insert(36, str(36))     
  
    # Check if it's removing the minimum correctly:  
    assert trueSomeSameElements.removeMinimum() == fakeSomeSameElements.removeMinimum()
    

# Create very big length instances of minMaxHeap and FakeMinMaxHeap with random
# elements and some elements that are gonna be repeated for sure and test if the 
# removeMaximum() method works:    
def test_SomeSameElementsRemoveMaximum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 35000:
    trueSomeSameElements = minMaxHeap(35000)
    fakeSomeSameElements= FakeMinMaxHeap(35000)   
    
    # Insert a random element and two identical 
    # elements every single time through the loop:    
    for k in range(10000):
        d = random.randint(1, 11000)
        trueSomeSameElements.insert(d, str(d))
        fakeSomeSameElements.insert(d, str(d))
        trueSomeSameElements.insert(22, str(22))
        trueSomeSameElements.insert(54, str(54))       
        fakeSomeSameElements.insert(22, str(22))
        fakeSomeSameElements.insert(54, str(54))       
        
    # Check if it's removing the maximum correctly:  
    assert trueSomeSameElements.removeMaximum() == fakeSomeSameElements.removeMaximum()    

    
# Create very big length instances of minMaxHeap and FakeMinMaxHeap with random
# elements and some elements that are gonna be repeated for sure and test if the 
# findMinimum() method works:        
def test_SomeSameElementsFindMinimum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 35000:
    trueSomeSameElements = minMaxHeap(35000)
    fakeSomeSameElements = FakeMinMaxHeap(35000)   
    
    # Insert a random element and two identical 
    # elements every single time through the loop:       
    for k in range(10000):
        d = random.randint(1, 11000)
        trueSomeSameElements.insert(d, str(d))
        fakeSomeSameElements.insert(d, str(d))
        trueSomeSameElements.insert(88, str(88))
        trueSomeSameElements.insert(19, str(19))        
        fakeSomeSameElements.insert(88, str(88))
        fakeSomeSameElements.insert(19, str(19))     

    # Check if it's finding the minimum correctly:  
    assert trueSomeSameElements.findMinimum() == fakeSomeSameElements.findMinimum()    


# Create very big length instances of minMaxHeap and FakeMinMaxHeap with random
# elements and some elements that are gonna be repeated for sure and test if the 
# findMaximum() method works:          
def test_SomeSameElementsFindMaximum():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 35000:
    trueSomeSameElements = minMaxHeap(35000)
    fakeSomeSameElements = FakeMinMaxHeap(35000)   
    
    # Insert a random element and two identical 
    # elements every single time through the loop:      
    for k in range(10000):
        d = random.randint(1, 11000)
        trueSomeSameElements.insert(d, str(d))
        fakeSomeSameElements.insert(d, str(d))
        trueSomeSameElements.insert(43, str(43))
        trueSomeSameElements.insert(78, str(78))    
        fakeSomeSameElements.insert(43, str(43))
        fakeSomeSameElements.insert(78, str(78))             
     
    # Check if it's finding the maximum correctly:    
    assert trueSomeSameElements.findMaximum() == fakeSomeSameElements.findMaximum()       
 
    
# Create very big length instances of minMaxHeap and FakeMinMaxHeap with random
# elements and some elements that are gonna be repeated for sure and test if both 
# have the same length:    
def test_SomeSameElementsLen():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a capacity of 35000:
    trueSomeSameElements = minMaxHeap(35000)
    fakeSomeSameElements = FakeMinMaxHeap(35000)   
    
    # Insert a random element and two identical 
    # elements every single time through the loop:     
    for k in range(10000):
        d = random.randint(1, 11000)
        trueSomeSameElements.insert(d, str(d))
        fakeSomeSameElements.insert(d, str(d))
        trueSomeSameElements.insert(53, str(53))
        trueSomeSameElements.insert(85, str(85))    
        fakeSomeSameElements.insert(53, str(53))
        fakeSomeSameElements.insert(85, str(85))  
     
    # Check if both have the same length:     
    assert len(trueSomeSameElements) == len(fakeSomeSameElements) 


# Torture test comparing the behavior of minMaxHeap and FakeMinMaxHeap:  
def test_Torture():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a length of 2000000:
    trueTorture = minMaxHeap(2000000)
    fakeTorture = FakeMinMaxHeap(2000000)   
    
    # Insert 1500000 random elements into both heaps:
    for k in range(1500000):
        d = random.randint(1, 10000000)
        trueTorture.insert(d, str(d))
        fakeTorture.insert(d, str(d))
    
    # Check that both have the same minimum, maximum and length:    
    assert trueTorture.findMinimum() == fakeTorture.findMinimum() 
    assert trueTorture.findMaximum() == fakeTorture.findMaximum()  
    assert len(trueTorture) == len(fakeTorture)
      
    # Remove 30 times the minimum or maximum (chosen randomly):  
    for d in range(30):
        choose = random.choice(["removeMinimum", "removeMaximum"])
        if choose == "removeMinimum":
            trueTorture.removeMinimum()
            fakeTorture.removeMinimum()
        else:
            trueTorture.removeMaximum()
            fakeTorture.removeMaximum()        
    
    # Check that both have the same minimum and length:    
    assert trueTorture.findMinimum() == fakeTorture.findMinimum()   
    assert len(trueTorture) == len(fakeTorture) 
    
    # Remove 50 times the minimum or maximum (chosen randomly): 
    for d in range(50):
        choose = random.choice(["removeMinimum", "removeMaximum"])
        if choose == "removeMinimum":
            trueTorture.removeMinimum()
            fakeTorture.removeMinimum()
        else:
            trueTorture.removeMaximum()
            fakeTorture.removeMaximum()          
     
    # Check that both have the same maximum and length:    
    assert trueTorture.findMaximum() == fakeTorture.findMaximum()       
    assert len(trueTorture) == len(fakeTorture) 


# Torture test comparing the behavior of minMaxHeap and FakeMinMaxHeap when it 
# is sure to assume that both have unique elements:      
def test_TortureUnique():
    # Create instances of minMaxHeap and FakeMinMaxHeap with a length of 2000000:
    trueTortureUnique = minMaxHeap(2000000)
    fakeTortureUnique = FakeMinMaxHeap(2000000)   
    
    # Create a set called unique to keep track of the items 
    # already inserted (to avoid duplicates):
    unique = set()
    
    # Insert 1500000 random elements into both heaps:
    for k in range(1500000):
        d = random.randint(1, 10000000)
        while d in unique:  
            d = random.randint(1, 10000000)      
            trueTortureUnique.insert(d, str(d))
            fakeTortureUnique.insert(d, str(d))  
        unique.add(d)
    
    # Assert both have the same minimum, maximum, and length:
    assert trueTortureUnique.findMinimum() == fakeTortureUnique.findMinimum() 
    assert trueTortureUnique.findMaximum() == fakeTortureUnique.findMaximum()          
    assert len(trueTortureUnique) == len(fakeTortureUnique) 
    
    # Remove the minimum from both 50 times:      
    for d in range(50):
        trueTortureUnique.removeMinimum()
        fakeTortureUnique.removeMinimum()   
    
    # Check that both have the same minimum:   
    assert trueTortureUnique.findMinimum() == fakeTortureUnique.findMinimum()   
    
    # Remove the maximum from both 30 times: 
    for d in range(30):
        trueTortureUnique.removeMaximum()
        fakeTortureUnique.removeMaximum()     
    
    # Check that both have the same maximum and length:        
    assert trueTortureUnique.findMaximum() == fakeTortureUnique.findMaximum()       
    assert len(trueTortureUnique) == len(fakeTortureUnique)

pytest.main(["-v", "-s", "test2__BIGHW.py"])