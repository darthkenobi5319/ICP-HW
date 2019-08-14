# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:39:02 2019

@author: Harry Zhenghan Zhang
"""

class phoneBook:
    def __init__(self):
        self.phonebook = dict()

    # This function adds a contact with one name a one number
    # @param:   contactName: A String specifying the contact name
    #           contactNumber: A number
    # @return:  returns no value.    
    def addContact(self,contactName,contactNumber):
        if contactName not in self.phonebook.keys():
            self.phonebook[contactName] = contactNumber
        else:
            print("User already exists")
        return

    # This fuction allows the user to change the phone number (add,delete,change)  
    # @param:   none
    # @return:  returns no value.
    def updateContact(self):
        print("1).Add number")
        print("2).Delete number")
        print("3).Change number")
        print("4).Change contact name")
        updateType = input("How would you like to update your information?:")
        if updateType == "1":
            contactName = input("Enter the contact name: ")
            contactNumber = input("Enter the contact number: ")
            self.addNumber(contactName,contactNumber)
        elif updateType == "2":
            contactName = input("Enter the contact name: ")
            contactNumber = input("Enter the contact number: ")
            self.deleteNumber(contactName,contactNumber)
        elif updateType == "3":
            contactName = input("Enter the contact name: ")
            contactNumber1 = input("Enter the contact number you want to change: ")
            contactNumber2 = input("Enter the contact number you want to change into: ")
            self.changeNumber(contactName,contactNumber1,contactNumber2)
        elif updateType == "4":
            contactName1 = input("Enter the contact name you want to change: ")
            contactName2 = input("Enter the contact name you want to change into: ")
            self.changeName(contactName1,contactName2)
        else:
            print("Invalid input:")
        return
    
    # This function add a number to a given user
    # @param:   contactName: A String specifying the contact name
    #           contactNumber: A number
    # @return:  returns no value.   
    def addNumber(self,contactName,contactNumber):
        if contactName in self.phonebook.keys():
            if contactNumber not in self.phonebook[contactName]:
                self.phonebook[contactName].append(contactNumber)
        else:
            print("User not found.")
        return

    # This function deletes a number to a given user
    # if there is only one number, the deletion of that would delete the contact entirely      
    # @param:   contactName: A String specifying the contact name
    #           contactNumber: A number
    # @return:  returns no value.     
    def deleteNumber(self,contactName,contactNumber):
        if contactName in self.phonebook.keys():
            if len(self.phonebook[contactName]) == 1:
                del self.phonebook[contactName]
            else:
                self.phonebook[contactName].remove(contactNumber)
        else:
            print("User not found.")
        return
    
    # This function changes a number to a given user
    # @param:   contactName: A String specifying the contact name
    #           contactNumber1: A number to change
    #           contactNumber2: A number to change into
    # @return:  returns no value.     
    def changeNumber(self,contactName,contactNumber1,contactNumber2):    
        if contactName in self.phonebook.keys():
            self.phonebook[contactName].remove(contactNumber1)
            self.phonebook[contactName].append(contactNumber2)
        else:
            print("User not found.")
        return
    
    
    
    
    # This function changes a name to a given user
    # @param:
    #           contactName1: A Name to change
    #           contactName2: A Name to change into
    # @return:  returns no value.     
    def changeName(self,contactName1,contactName2):    
        if contactName1 in self.phonebook.keys():
            if contactName2 in self.phonebook.keys():
                self.phonebook[contactName2].extend(self.phonebook[contactName1])
                del self.phonebook[contactName1]
            else:
                self.phonebook[contactName2] = self.phonebook[contactName1]
        else:
            print("User not found.")
        return
    
    
    
    # This function deletes a contact by name, along with all the numbers.    
    # @param:   contactName: A String specifying the contact name
    # @return:  returns no value. 
    def deleteContact(self,contactName):
        if contactName in self.phonebook.keys():
            del self.phonebook[contactName]
        else:
            print("User not found.")
        return
    
    # This functions finds all the numbers by a given contact name
    # @param:   contactName: A String specifying the contact name
    # @return:  returns the numbers or send an error message. 
    def findContact(self,contactName):
        if contactName in self.phonebook.keys():
            self.phonebook[contactName].sort()
            return self.phonebook[contactName]
        else:
            return "User not found."
    
    # This function displays the entire book.
    # Ordered by the names of contacts. 
    # @param:   none
    # @return:  returns no value. 
    def __str__(self):
        orderedKeys = list(self.phonebook.keys())
        if len(orderedKeys) == 0:
            return "The phonebook is empty!"
        orderedKeys.sort()
        result = ''
        for i in orderedKeys:
            self.phonebook[i].sort()
            subresult = ''
            for j in self.phonebook[i]:
                subresult += str(j) 
            result += ("Contact: " + i + " | Numbers: " + subresult + '\n')
        return result

if __name__ == "__main__":
    cont = True
    phonebook = phoneBook()
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
            phonebook.addContact(contactName,contactNumbers)
            continue
        
        elif command == '2':
            phonebook.updateContact()
            continue
        
        elif command == '3': 
            contactName = input("Please enter the contact name you want to delete:")
            phonebook.deleteContact(contactName)
            continue
        
        elif command == '4': 
            contactName = input("Please enter the contact name you want to look up:")
            print(phonebook.findContact(contactName))
            continue
        elif command == '5':
            print(phonebook)
            continue
        elif command == '6':
            cont = False
            break
        else:
            print("Invalid input.")