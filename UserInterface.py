#!/usr/bin/env python
# coding: utf-8

# In[23]:


def addPatient(unreceived, received, dead):
    lastName = str(input("Please enter a last name: "))
    while lastName=='':
        lastName = str(input("Please enter a last name: "))
        
    firstName = str(input("Please enter a first name: "))
    while firstName=='':
        lastName = str(input("Please enter a first name: "))
        
    ID = len(unreceived)+len(received)+len(dead)+1
    
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
            unreceived.append(addPatient(unreceived, received, dead))
            command = input("What would you like to do? ")
            
        elif command == "list":
            listToPrint = str(input("Which list would you like to print? ('received', 'unreceived', or 'dead') "))
            while listToPrint != 'received' and listToPrint != 'unreceived' and listToPrint != 'dead':
                listToPrint = str(input("Which list would you like to print? ('received', 'unreceived', or 'dead') "))
            if listToPrint == 'received':
                print(received)
            if listToPrint == 'unreceived':
                print(unreceived)
            if listToPrint == 'dead':
                print(dead)
    
            command = input("What would you like to do? ")
            
        elif command == "move":
            pass
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

        elif command == "quit":
            return unreceieved, received, dead
        
        else:
            command = str(input("Please enter a valid command: "))
            
        
            
        
unreceived = []
received = []
dead = []
runProgram(unreceived, received, dead)


