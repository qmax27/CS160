#!/usr/bin/env python
# coding: utf-8

# In[27]:


class Node:             # complexity of this class is 1 because each of these methods will run one time when called
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


class UnorderedList:        #O(N) complexity due to iterative search method

    def __init__(self):
        self.head = None

    def isEmpty(self):                 #O(1)
        return self.head == None

    def add(self, item):               #O(1)
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):                     #O(N)
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item, update):                            #O(N)
        current = self.head
        found = False
        while current != None and not found:
            element = current.getData()
            
            if element[2] == item:
                found = True
                print(current.getData())
                if update == "Y":
                    current = updateRecord(current.getData())
            else:
                current = current.getNext()

        return found

    def remove(self, item):                        #O(N)
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
            if previous == None:  
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            return "List is empty"  #
    def printList(self):                                 #O(N)
        n = 0
        ln = self.size()
        c_val = self.head
        final_list = []
        if not self.isEmpty():
            while n < ln:
                final_list += [c_val.getData()]
                c_val = c_val.getNext()
                n += 1
            print(final_list)
        else:
            print('list is empty')
class BinHeap:                  #O(n^2 log n) complexity.
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i): #O(N) complexity thanks to iterative sorting
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):                                   #O(N)
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):      #O(N) complexity thanks to iterative sorting
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):      #O(1) as every statement will run once herein when called
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


    def fuldel(self):   #calls the sort method 'percdown' but only runs each statement once
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval


    def delMin(self, i):        #O(1) complexity, every line only runs once
        retval = self.heapList[1]
        i.add(retval)
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)

    def buildHeap(self, alist): #O(N^2) complexity due to iterative loop that depends on length of list given and the calling of a O(N) sort within
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def binarySearchHelper(self, item, start, end):     #O(log n) complexity. Function searches recursively
        if abs(end - start) <= 1:
            return False, 'N/a'
        midpoint = (start + end) // 2
        if self.heapList[midpoint] == item:
            return True, midpoint
        if item < self.heapList[midpoint]:
            return self.binarySearchHelper(item, start, midpoint)
        return self.binarySearchHelper(item, midpoint, end)

    def transfer(self, i, l):           #O(1) complexity as every line runs once at most
        d_p = self.binarySearchHelper(i, 0, self.currentSize)
        if d_p[0] == True:
            l.add(i)
            self.heapList[d_p[1]] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop(d_p[1])
            self.percDown(d_p[1])


def addPatient(unreceived, received, dead, masterList):         #O(1) compexity. Unless user continually enters invalid entries
    lastName = str(input("Please enter a last name: "))
    while lastName=='':
        lastName = str(input("Please enter a last name: "))
        
    firstName = str(input("Please enter a first name: "))
    while firstName=='':
        lastName = str(input("Please enter a first name: "))

    ID = unreceived.currentSize+(received.size())+(dead.size())+1
    
    priority = int(input("Please enter a priority number between 1-10: "))
    while priority <= 0 or priority == '' or priorityUsed(priority, masterList):
        priority = int(input("Priority already used or invalid: "))

    patient = [lastName, firstName, ID, priority]
    return patient


def updateRecord(element,unreceived):              #O(1) compexity, Unless user changes patient priority
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
        while priority <= 0 or priority == '' or priorityUsed(priority, masterList):
            priority = int(input("Please enter a priority number between 1-10(may have been used already): "))
        temp = UnorderedList()
        
        temp = element[3]
        unreceived.insert(priority)

        element[3] = priority
    return temp


def show(masterList, unreceived):               #O(n) complexity due to iterative list that depends on the length of the list
            ID = int(input("Please enter a patient's ID "))
            while ID == '':
                ID = int(input("Please enter a patient's ID "))
            found = False
            if ID < 1:
                found = False
            else:
                update = input("Do you need to update the patient's record? (Input Y or N) ")
                while update != "Y" and update != "N":
                    update = input("Input 'Y' or 'N': ")

                for i in range(len(masterList)):
                    if masterList[i][2] == ID:
                        found = True
                        t_lis = UnorderedList()
                        unreceived.transfer(ID, t_lis)
                        print(masterList[i])
                        if update == 'Y':
                            temp = updateRecord(masterList[i],unreceived)
                            print(temp)
                            return temp

            if found == False:
                print("***Patient not found***")


def priorityFinder(ID, masterList):         #O(1)
    element = masterList[ID-1]
    return element[3]
def priorityUsed(priority, masterList):     #O(N), iterative search
    for elements in masterList:
        if elements[3]==priority:
            return True
    return False
            
    
def runProgram(master, unreceived, received, dead):         #Overall complexity depends on how many commands the user calls. It can be as high as n^2 and as low as log n
    print("'help' = print all commands")
    command = input("What would you like to do? ")
    while command != 'quit':
        if command == 'help':
            print("'add' = add a patient to the unreceived list")
            print("'list' = list all records for a particular list")
            print("'move' = move a patient from the unrecieved list to either the received or dead lists")
            print("'moveTop' = move top patient from the unrecieved list to either the received or dead lists")
            print("'show' = shows/updates a specified patient's record")
            print("'help' = print all commands")
            print("'quit' = quit the program")

            command = input("What would you like to do? ")
            
        elif command == 'add':
            patient = addPatient(unreceived, received, dead, masterList)
            print(patient)
            temp = int(patient[3])
            unreceived.insert(temp)
            masterList.append(patient)
            command = input("What would you like to do? ")
            
        elif command == "list":
            listToPrint = str(input("Which list would you like to print? ('master', 'received', 'unreceived', or 'dead') "))
            while listToPrint != 'received' and listToPrint != 'unreceived' and listToPrint != 'dead' and listToPrint != 'master':
                listToPrint = str(input("Which list would you like to print? ('master', 'received', 'unreceived', or 'dead') "))
            if listToPrint == 'received':
                received.printList()
            if listToPrint == 'unreceived':
                print(str(unreceived.heapList))
            if listToPrint == 'dead':
                dead.printList()
            if listToPrint == 'master':
                print(masterList)
    
            command = input("What would you like to do? ")
            
        elif command == "moveTop":
            moveCom = input("Where do you want to move the patient? (received, dead, or cancel) ")
            while moveCom != 'received' and moveCom != 'dead' and moveCom != 'cancel':
                moveCom = input("Where do you want to move the patient? (received, dead, or cancel) ")
            if moveCom == 'received':
                unreceived.delMin(received)
            elif moveCom == 'dead':
                unreceived.delMin(dead)
            
            command = input("What would you like to do? ")
        elif command == "move":
            ID = int(input("Please enter a patient's ID "))
            while ID == '':
                ID = int(input("Please enter a patient's ID "))   
            moveCom = input("Where do you want to move the patient? (received, dead, or cancel) ")
            while moveCom != 'received' and moveCom != 'dead' and moveCom != 'cancel':
                moveCom = input("Where do you want to move the patient? (received, dead, or cancel) ")
            priority = priorityFinder(ID, masterList)
            if moveCom != 'cancel':
                if moveCom == "received":
                    unreceived.transfer(priority, received)
                else:
                    unreceived.transfer(priority, dead)
            command = input("What would you like to do? ")
                

        elif command == "show":
            temp = show(masterList, unreceived)
            if temp !=None:
                tempList = UnorderedList()
                unreceived.transfer(temp,tempList)
            command = input("What would you like to do? ")          
        
        else:
            command = str(input("Please enter a valid command: "))
            
    return masterList, unreceived, received, dead
            
        
unreceived = BinHeap()
received = UnorderedList()
dead = UnorderedList()
masterList = []
lists = runProgram(masterList, unreceived, received, dead)

masterList = lists[0]
unreceived = lists[1]
received = lists[2]
dead = lists[3]
newlist = unreceived.heapList
newlist.pop(0)
print("Master list: " +str(masterList))
print("Unreceived list: " +str(newlist))
print("Received list: ", end = ' ')
received.printList()
print("Dead list: ", end = ' ')


dead.printList()

