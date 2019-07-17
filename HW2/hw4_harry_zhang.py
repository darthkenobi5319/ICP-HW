# Homework #4

# In all the exercises that follow, insert your code directly in this file
# and immediately after each question.
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

In the paragraph below, all sentences end with an exclamation mark.

1.1) Use .replace() to remove any newline characters in the string
paragraph_str, storing the result back in the same variable
(paragraph_str).

1.2) Write a program that uses the .split() function to break down the
string paragraph_str into the 4 sentences it contains. Store the
returned list of sentences in a variable called sentence_list.

1.3) Use the .strip() function to remove any unnecessary whitespace
characters from the edges of each of the 4 sentences. Store each
stripped sentence in the same position in the list sentence_list,
effectively updating (ie, modifying) each sentence in the list. Notice
that each of the sentences is now lacking the punctuation mark that
marked its end. (You don't need to worry / do anything about that.)
  
1.4) Using the .capitalize() function, again modify each sentence in
sentence_list so that each sentence has its first letter in upper case
and all other characters in lower case.
 
1.5) Use the .join() function to glue back the 4 modified sentences
into a string, using a period at the end of every sentence. (The
punctuation in the paragraph will therefore be different from what it
was originally.) Store the result of .join() in a variable called
revised_paragraph and print that variable. 

"""

paragraph_str = """ programming is such a blast!    if you ask me, this is
pretty much as cool as it gets! i even get slightly high from coding!
do it while listening to some bachata and it becomes the ultimate
legal high..."""


# Answer to Question 1.1
paragraph_str = paragraph_str.replace('\n','')
print(paragraph_str)
# Answer to Question 1.2
sentence_list = paragraph_str.split('!')
print(sentence_list)
# Answer to Question 1.3
for i in range(len(sentence_list)):
    sentence_list[i] = sentence_list[i].strip()
print(sentence_list)
# Answer to Question 1.4
for i in range(len(sentence_list)):
    sentence_list[i] = sentence_list[i].capitalize()
print(sentence_list)
# Answer to Question 1.5
newList=[]
for i in sentence_list:
    newList.append(i)
    newList.append(".")
revised_paragraph = "".join(newList)
print(revised_paragraph)
"""

Question 2
  
2.1) Create a list called 'friends' containing the first names of 5
friends of yours, ranked in ascending chronological order based on
when you met them. (The oldest friend goes first; the most recent one
goes last.) Print that list.

2.2) Suppose you realize that you have recently made a new friend,
most likely another hardcore Python geek taking our course. Use a
function to add their name to the end of the list and print the
updated list.

2.3) Print the name of the second oldest friend on your list, using
the % operator or .template(). Supposing Maria is your second oldest
friend on the list, then your code should print:
  
     Maria is the second oldest friend on my friends list.

2.4) Using a single statement, replace the third and fourth friends on
your list with two new names of your choice. The rest of your list
should remain unchanged. Print the list 'friends' again.

2.5) Unfortunately, it turned out that Python geeks cannot be trusted
and you are no longer friends with the person you added in Question
2.2. Remove them from the list 'friends' and print the list again.

2.6) Print the names of the friends on your list ordered
alphabetically, while leaving the original list 'friends' unchanged.

"""

# Answer to Question 2.1
friends = ["Fischer","Karen","Tony","James","Andy"]
print(friends)
# Answer to Question 2.2
friends.append("Zhixing")
print(friends)
# Answer to Question 2.3
output = "%s is the second oldest friend on my friends list." % friends[1]
print(output)
# Answer to Question 2.4
friends[2:4] = ["Kaiyi","Steven"]
print(friends)
# Answer to Question 2.5
friends.pop()
print(friends)
# Answer to Question 2.6
new_friends = friends.copy()
for i in range(len(new_friends)):
    new_friends[i] = new_friends[i].upper()
new_friends.sort()
for i in range(len(new_friends)):
    new_friends[i] = new_friends[i].capitalize()
print(new_friends)
print(friends)
