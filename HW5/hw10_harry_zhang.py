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
#
# 3) WHENEVER A QUESTION DOES NOT SPECIFY A PARTICULAR WAY TO DO SOMETHING,
#    THEN YOU CAN DO IT *ANY* WAY. :-)

"""

In this assignment, you will practice writing and reading data to/from
files. 


Question 1

Write a short program that writes the following two lines

     Good morning! There is nothing I love more than coding after waking up!
     This is the second line of this file. Goodbye!
     
to a file called 'morning.txt'. Notice that, to write multiple lines,
the string must contain one or more newline characters (\n). Also,
remember that to properly write to a file, you must .flush() or .close()
it.

Note: you do *not* need to upload the file morning.txt onto NYU Classes.

"""

# Answer to Question 1
fp = open('morning.txt','w')
print('Good morning! There is nothing I love more than coding after waking up!',file = fp)
print('This is the second line of this file. Goodbye!',file = fp)
fp.close()

"""

Question 2

On NYU Classes, next to the file you are currently reading, you will
find a file called 'hw10-data.txt'. Download that file and place it in the
same directory where you are writing your homework assignment.

Each line in hw10-data.txt contains 3 values separated by tabs. As we
saw in class, a tab is represented as \t. The file contents are


    Mary	54	New York, NY
    Sergio	28	Cranford, NJ
    Natalia	32	Portland, ME
    Tisha	64	Davis, CA

where columns represent the name, the age and the city of residence
pulled from a database containing personal information.

Write a program that reads the file hw10-data.txt and, for each person
listed in that file, prints out a message providing the information we
have about them. Your program should output:
    
    Mary is 54 years old and lives in New York, NY.
    Sergio is 28 years old and lives in Cranford, NJ.
    Natalia is 32 years old and lives in Portland, ME.
    Tisha is 64 years old and lives in Davis, CA.

Please note your program should *not* assume that there are only 4
records in the file. Instead, it should process all lines in the file
hw10-data.txt, regardless of their number.

"""

# Answer to Question 2
fp = open('hw10-data.txt','r')
for i in fp:
    line = i.strip('\n').split('\t')
    print('%s is %s years old and lives in %s'%(line[0],line[1],line[2]))
fp.close()

"""

Question 3

This question asks you to record data your code retrieved from an
online source to a file.

To save time, you will base it on your answer to Question 2 of our
previous homework (Homework 9). You can either copy paste your own
answer into this file or you can use the sample answer we have posted
on NYU Classes. Both approaches are totally fine.

Homework 9 used the Star Wars API. Question 2.1 in that homework asked
you to retrieve information about _all_ starships in Star Wars (i.e.,
*not* just the first batch of 10 starships sent by the server) and
save it in a list.

Modify that code so that it creates a file called 'starships.txt' and
writes some of the information about each of the starships to that
file. There should be one line for each starship. Each line in that
file should contain the following information about a starship:
    
    name,crew,length
    
where 'name', 'crew' and 'length' are the values obtained from the API
for that particular starship. If any value is listed as 'unknown' or
otherwise unavailable, your code should insert the string 'NA' into
that field in the file.

Note 1: Your answer to this question should include all required code
to retrieve the information from the Star Wars API as well as write it
to the file starships.txt. Probably you will want to start by copying
your answer to Question 2.1 of HW9 into the file you in which you are
writing HW10.
    
Note 2: There are main two approaches to solve this problem. The first
is for your code to retrieve information about _all_ the starships
first and then write it, in a single go, to the file starships.txt.
The second approach is for your code to open the file in 'append' mode
and write to the file multiple times, each time recording information
about the new batch of starships it just retrieved. Both approaches
are perfectly fine. (For extra practice, consider implementing both.
:-) However, *please only submit one* in your homework.)


Optional: If you want practice in structuring your code in a more
"realistic" way that will serve you well when developing more complex
programs, consider organizing your answer to this question into
functions. You can divide your code into small self-contained "units"
(i.e., functions), each of them doing a specific task. As you might
remember, you can define functions to receive any data they need
through their arguments and pass on any results of their work through
the "return" statement at their end. Functions can receive as
arguments and/or return at the end any number of Python variables of
any type (e.g., strings, numbers, lists, dictionaries or the file
handles we use to read from/write to files). Structuring your code in
this way so that it uses functions defined by you is *totally
optional*. It is *not* required to get full credit for this question. 
    
"""

# Answer to Question 3


import requests
# This function gives the dictionary fo all starship information
# @param: 
# @return:  dictionary containing all starship information.
#           The keys are ships' names and the values are all its information,excluding the name
def get_starships():
    url = "https://swapi.co/api/starships/?format=json"
    starships = dict()
    while url != None:
        r = requests.get(url)
        r_json = r.json()
        results = r_json['results']
        for i in results:
            name = i['name']
            del i['name']
            starships[name] = i 
        url = r_json['next']     
    return starships

def writeInfo(starships):
    fp = open('starships.txt','w')
    for i in starships.keys():
        name = i
        if starships[i]['crew'] != 'unknown':
            crew = starships[i]['crew']
        else:
            crew = 'NA'
        if starships[i]['length'] != 'unknown':
            length = starships[i]['length']
        else:
            length = 'NA'
        print(name,crew,length,sep = ',',file = fp)
    fp.close()
    return

writeInfo(get_starships())