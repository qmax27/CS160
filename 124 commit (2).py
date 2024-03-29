#!/usr/bin/env python
# coding: utf-8

# In[67]:


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        if not self.isEmpty() or current != None:  # in order to make this a stack we would have to make it so the item is only removed if it equals the head so we would have the boolean statement check if the head equals the item removed
            while not found:
                if current.getData() == item:  # to make unordered list queue
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            if previous == None:  # What happens when the list is empty in this function?
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            return "List is empty"  #


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


    def fuldel(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval


    def delMin(self, i):
        retval = self.heapList[1]
        i.add(retval)
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def binarySearchHelper(self, item, start, end):
        if abs(end - start) <= 1:
            return False
        midpoint = (start + end) // 2
        if self.heapList[midpoint] == item:
            return True, midpoint
        if item < self.heapList[midpoint]:
            return self.binarySearchHelper(item, start, midpoint)
        return self.binarySearchHelper(item, midpoint, end)

    def transfer(self, i, l):
        d_p = self.binarySearchHelper(i, 0, self.currentSize)
        if d_p[0] == True:
            l.add(i)
            self.heapList[d_p[1]] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop(d_p[1])
            self.percDown(d_p[1])
        else:
            print('Patient not currently awaiting organ')


def addPatient(unreceived, received, dead):
    lastName = str(input("Please enter a last name: "))
    while lastName=='':
        lastName = str(input("Please enter a last name: "))
        
    firstName = str(input("Please enter a first name: "))
    while firstName=='':
        lastName = str(input("Please enter a first name: "))

    ID = unreceived.currentSize+(received.size())+(dead.size())+1
    
    priority = int(input("Please enter a priority number between 1-10: "))
    while priority <= 0 or priority == '':
        priority = int(input("Please enter a priority number between 1-10: "))

    patient = [lastName, firstName, ID, priority]
    return patient

def updateRecord(element):
    update = input("Do you need to update the patient's last name? (Input Y or N)")
    while update != "Y" and update != "N":
        update = input("Input 'Y' or 'N': ")
    if update == 'Y':
        lastName = input("Please input a last name")
        element[0] = lastName
    
    update = input("Do you need to update the patient's first name? (Input Y or N)")
    while update != "Y" and update != "N":
        update = input("Input 'Y' or 'N': ")
    if update == 'Y':
        firstName = input("Please input a first name")
        element[1] = firstName
    
    update = input("Do you need to update the patient's priority? (Input Y or N)")
    while update != "Y" and update != "N":
        update = input("Input 'Y' or 'N': ")
    if update == 'Y':
        priority = int(input("Please input a priority number between 1-10: "))
        while priority <= 0 or priority == '':
            priority = int(input("Please enter a priority number between 1-10: "))
        element[3] = priority
    return element
    
    
        

def runProgram(unreceived, received, dead):
    print("'help' = print all commands")
    newHeap = BinHeap()
    newHeap.buildHeap(unreceived)
    unreceived = newHeap
    command = input("What would you like to do? ")
    while command != 'quit':
        if command == 'help':
            print("'add' = add a patient to the unreceived list")
            print("'list' = list all records for a particular list")
            print("'move' = move a patient from the unrecieved list to either the received or dead lists")
            print("'show' = shows a specified patient's record")
            print("'help' = print all commands")
            print("'quit' = quit the program")
            command = input("What would you like to do? ")
            
        elif command == 'add':
            patient = addPatient(unreceived, received, dead)
            print(patient)
            unreceived.insert(patient)
            command = input("What would you like to do? ")
            
        elif command == "list":
            listToPrint = str(input("Which list would you like to print? ('received', 'unreceived', or 'dead') "))
            while listToPrint != 'received' and listToPrint != 'unreceived' and listToPrint != 'dead':
                listToPrint = str(input("Which list would you like to print? ('received', 'unreceived', or 'dead') "))
            if listToPrint == 'received':
                print(received)
            if listToPrint == 'unreceived':
                helperList = unreceived
                h2 = UnorderedList()
                while helperList.currentSize > 0:
                    helperList.delMin(h2)
                print(h2)
                print(unreceived)
            if listToPrint == 'dead':
                print(dead)
    
            command = input("What would you like to do? ")
            
        elif command == "moveTopPatient":
            moveCom = input("Where do you want to move the patient? (received, dead, or cancel) ")
            while moveCom != 'received' and moveCom != 'dead' and moveCom != 'cancel':
                moveCom = input("Where do you want to move the patient? (received, dead, or cancel) ")
            if moveCom == 'received':
                unreceived.delMin(received)
            elif moveCom == 'dead':
                unreceived.delMin(dead)
            
            command = input("What would you like to do? ")
            
        elif command == "show":
            ID = int(input("Please enter a patient's ID "))
            while ID == '':
                ID = int(input("Please enter a patient's ID "))
            update = input("Do you need to update the patient's record? (Input Y or N) ")
            while update != "Y" and update != "N":
                update = input("Input 'Y' or 'N': ")
                    
            count = 0
            found = False
            
            while found == False and ((count) < len(unreceived)):
                element = unreceived[count]
                if element[2] == ID:
                    found = True
                    print(element)
                    if update == 'Y':
                        element = updateRecord(element)
                count += 1
                
            count = 0
            while found == False and ((count) < len(received)):
                element = unreceived[count]
                if element[2] == ID:
                    found = True
                    print(element)
                    if update == 'Y':
                        element = updateRecord(element)
                count += 1
                
            count = 0
            while found == False and ((count) < len(dead)):
                element = dead[count]
                if element[2] == ID:
                    found = True
                    print(element)
                    if update == 'Y':
                        element = updateRecord(element)
                count += 1
            if found == False:
                print("***Patient not found***")
                
            command = input("What would you like to do? ")          
        
        else:
            command = str(input("Please enter a valid command: "))
            
    return unreceived, received, dead
            
        
unreceived = [['Quenton','Max',1,1]]
received = UnorderedList()
dead = UnorderedList()
lists = runProgram(unreceived, received, dead)

unreceived = lists[0]
received = lists[1]
dead = lists[2]
print("Unreceived list: " +str(unreceived))
print("Received list: " +str(received))
print("Dead list: " +str(dead))

