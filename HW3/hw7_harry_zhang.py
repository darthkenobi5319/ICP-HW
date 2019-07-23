# In all the exercises that follow, insert your code directly in this file
# where you find a comment saying "Answer to Question [...]"
#
# IMPORTANT NOTES: 
#
# 1) THIS IS A PROGRAMMING COURSE. :-) THIS MEANS THAT THE ANSWERS TO THESE QUESTIONS
# ARE MEANT TO BE DONE IN CODE AS MUCH AS POSSIBLE. E.G., WHEN A QUESTION SAYS "COUNT
# THE NUMBER OF TIMES THAT [...]" YOU SHOULD INTERPRET THIS AS "WRITE CODE THAT COUNTS
# THE NUMBER OF TIMES THAT [...]". USE YOUR BEST JUDGMENT AND YOU WILL DO FINE. :-)
#
# 2) WHEN A QUESTION PROVIDES A VALUE FOR YOU TO USE IN COMPUTATIONS, FIRST STORE IT IN
# A VARIABLE AND WRITE CODE THAT MAKES USE OF THAT VARIABLE.

"""

Question 1

1.1) Create an empty dictionary called 'addresses'. 

The dictionary you just created will map names to addresses. A
person's name (stored as a string) will be the KEY and that person's
address (stored as a string) will be the VALUE.

1.2) Insert into the dictionary 'addresses' the names and addresses of
two (possibly imaginary) friends of yours.

1.3) Create a second empty dictionary called 'ages'. 

The dictionary you just created will map names to ages. A person's
name (stored as a string) will be the KEY and that person's age
(stored as an integer) will be the VALUE.

1.4) Insert into the dictionary 'ages' the names and ages of the same
two (possibly imaginary) friends of yours. (Note: these two friends
must be the same two friends that you inserted into the dictionary
'addresses' earlier.)

1.5) Using a for loop, print out, for each friend, the information
available about them in a single sentence. For example, if your
dictionaries contained the age and address of your friends 'Mary
Jones' and 'Miguel Hernandez', then your code would output:
    
    Mary Jones is 20 years old and lives at 28 Union St, Brooklyn, NY.
    Miguel Hernandez is 21 years old and lives at 394 Fifth Avenue, New York, NY.
    
    
"""

# Answer to Question 1.1
address = dict()
# Answer to Question 1.2
address["Karen"] = "1205, 140 E 14TH St, New York, NY"
address["Tony"] = "1225, 140 E 14TH St, New York, NY"  
# Answer to Question 1.3
ages = dict()
# Answer to Question 1.4
ages["Karen"] = 22
ages["Tony"] = 22
# Answer to Question 1.5
for i in address.keys():
    if i in ages.keys():
        print("%s is %d years old and lives at %s." % (i,ages[i],address[i]))
"""

Question 2

As briefly mentioned in class, dictionaries can store other complex
data structures as the VALUE in a (KEY, VALUE) pair. In this question
you will expand on the phonebook example we created in class. 

2.1) Create an empty dictionary called contacts. 

The KEY in this dictionary will be the name of a contact (stored as a
string). The VALUE in this dictionary will be a list with three
elements: the first element will be a phone number (stored as a
string), the second an email address (stored as a string) and the
third their age (stored as an integer).

2.2) Insert information for three imaginary contacts of yours in the
dictionary contacts. 

2.3) Using input(), ask the user to enter an age. Then, using a for
loop and if statement, print the name and phone number for all
contacts that are either of that age or older. If no contacts of or
above that age are found, your code should report that to the user.
For example, suppose you have three friends in contacts with the data:

   Name:  Julia
   Phone: 384-493-4949 
   Email: john@example.org 
   Age:   34

   Name:  Alfred
   Phone: 784-094-4520 
   Email: alfred@example.org 
   Age:   49
   
   Name:  Sam
   Phone: 987-099-0932 
   Email: sam@samsdomain.ca
   Age:   28

Then, your code asks the user to specify a minimum age. In the example
below, the user enters the age '30':
       
     What is the minimum age? 30
   
Your code should then print the name and phone number of everyone who
is 30 years old or older:
       
     Julia is 34 years old and can be reached at 384-493-4949. 
     Alfred is 49 years old and can be reached at 784-094-4520.
   
If the user were to enter (for example) 50 at the prompt above, your
code should have instead printed the message:
    
     Sorry, you do not have any contacts that are 50 or older.
     
"""

# Answer to Question 2.1
contacts = dict()
# Answer to Question 2.2
contacts["Julia"] = {"Phone":"384-493-4949","Email":"john@example.org","Age":34}
contacts["Alfred"] = {"Phone":"784-094-4520","Email":"alfred@example.org","Age":49}
contacts["Sam"] = {"Phone":"987-099-0932","Email":"sam@samsdomain.ca","Age":28}
# Answer to Question 2.3
threshold = int(input("What is the minimum age?"))
temp = 0
for i in contacts.keys():
    if contacts[i]["Age"] >= threshold:
        temp += 1
        print("%s is %d years old and can be reached at %s." % (i,contacts[i]["Age"],contacts[i]["Phone"]))
if temp == 0:
    print("Sorry, you do not have any contacts that are %d or older." % threshold)