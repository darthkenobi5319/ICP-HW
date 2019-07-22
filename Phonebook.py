# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:39:02 2019

@author: Harry Zhenghan Zhang
"""
phonebook = dict()
cont = True

# This function adds a contact with one name a one number
# @param:   contactName: A String specifying the contact name
#           contactNumber: A number
# @return:  returns no value.    
def addContact(contactName,contactNumber):
    if contactName not in phonebook.keys():
        phonebook[contactName] = contactNumber
    else:
        print("User already exists")
    return

# This fuction allows the user to change the phone number (add,delete,change)  
# @param:   none
# @return:  returns no value.
def updateContact():
    print("1).Add number")
    print("2).Delete number")
    print("3).Change number")
    updateType = input("How would you like to update your information?:")
    if updateType == "1":
        contactName = input("Enter the contact name: ")
        contactNumber = input("Enter the contact number: ")
        addNumber(contactName,contactNumber)
    elif updateType == "2":
        contactName = input("Enter the contact name: ")
        contactNumber = input("Enter the contact number: ")
        deleteNumber(contactName,contactNumber)
    elif updateType == "3":
        contactName = input("Enter the contact name: ")
        contactNumber1 = input("Enter the contact number you want to change: ")
        contactNumber2 = input("Enter the contact number you want to change into: ")
        changeNumber(contactName,contactNumber1,contactNumber2)
    else:
        print("Invalid input:")
    return
    
# This function add a number to a given user
# @param:   contactName: A String specifying the contact name
#           contactNumber: A number
# @return:  returns no value.   
def addNumber(contactName,contactNumber):
    if contactName in phonebook.keys():
        if contactNumber not in phonebook[contactName]:
            phonebook[contactName].append(contactNumber)
    else:
        print("User not found.")
    return

# This function deletes a number to a given user
# if there is only one number, the deletion of that would delete the contact entirely      
# @param:   contactName: A String specifying the contact name
#           contactNumber: A number
# @return:  returns no value.     
def deleteNumber(contactName,contactNumber):
    if contactName in phonebook.keys():
        if len(phonebook[contactName]) == 1:
            del phonebook[contactName]
        else:
            phonebook[contactName].remove(contactNumber)
    else:
        print("User not found.")
    return

# This function changes a number to a given user
# @param:   contactName: A String specifying the contact name
#           contactNumber1: A number to change
#           contactNumber2: A number to change into
# @return:  returns no value.     
def changeNumber(contactName,contactNumber1,contactNumber2):    
    if contactName in phonebook.keys():
        phonebook[contactName].remove(contactNumber1)
        phonebook[contactName].append(contactNumber2)
    else:
        print("User not found.")
    return

# This function deletes a contact by name, along with all the numbers.    
# @param:   contactName: A String specifying the contact name
# @return:  returns no value. 
def deleteContact(contactName):
    if contactName in phonebook.keys():
        del phonebook[contactName]
    else:
        print("User not found.")
    return

# This functions finds all the numbers by a given contact name
# @param:   contactName: A String specifying the contact name
# @return:  returns the numbers or send an error message. 
def findContact(contactName):
    if contactName in phonebook.keys():
        phonebook[contactName].sort()
        return phonebook[contactName]
    else:
        return "User not found."

# This function displays the entire book.
# Ordered by the names of contacts. 
# @param:   none
# @return:  returns no value. 
def displayBook():
    orderedKeys = list(phonebook.keys())
    if len(orderedKeys) == 0:
        print("The phonebook is empty!")
        return
    orderedKeys.sort()
    for i in orderedKeys:
        phonebook[i].sort()
        print("Contact:",i,"|","Numbers:",phonebook[i],sep = ' ')
    return


while cont == True:
    print("------------------------------------")
    print("What do you want to do?")
    print("1).Add a contact")
    print("2).Update a contact")
    print("3).Delete a contact")
    print("4).Lookup number for a person")
    print("5).Display the phonebook")
    print("6).Quit")
    print("-----------------------------")
    command = input("Please make your selection: ")
    
    if command == '1':
        contactName = input("Please Enter user name:")
        contactNumbers = []
        temp = True
        while temp:
            contactNumbers.append(input("Please input a phone number:"))
            if (input("Add another number?(Y/N)").upper() != "Y"):
                temp = False
        addContact(contactName,contactNumbers)
        continue
    
    elif command == '2':
        updateContact()
        continue
    
    elif command == '3': 
        contactName = input("Please enter the contact name you want to delete:")
        deleteContact(contactName)
        continue
    
    elif command == '4': 
        contactName = input("Please enter the contact name you want to look up:")
        print(findContact(contactName))
        continue
    elif command == '5':
        displayBook()
        continue
    elif command == '6':
        cont = False
        break
    else:
        print("Invalid input.")