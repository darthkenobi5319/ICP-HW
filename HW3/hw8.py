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

1.1) Using the module requests, send a request for the NBC New York
weather page located at

     http://www.nbcnewyork.com/weather/

1.2) If the request succeeds, print the message 

     Success! Retrieved the page

and store the HTML of the page you have downloaded in a variable
called 'html'. If the request failed, print the message 

     Error: downloading failed

and terminate your program by running the commands

    import sys
    sys.exit(1)

"""

# Answer to Question 1.1

# Answer to Question 1.2





"""

Question 2

Assume the request above succeeded and the string variable 'html'
contains the NBC New York weather page.

Note: Sometimes the automatic location detection of the site gets your
location wrong and shows you the weather for some other part of NY
state. Do not worry about that, as it will have no impact on your
grade.

Using the module BeautifulSoup, answer the following questions:

2.1) Extract from the HTML the current temperature prominently
displayed on the page and print it out. Please check the screenshot
posted as an attachment to this assignment on NYU Classes to get a
clear indication of what you should be looking for. Obviously, by the
time you complete this assignment most likely the temperature on the
page will be a different one (and the page might have been slightly
redesigned, as it often happens): the screenshot is meant merely to
show you its position on the page. You might need to use some string
manipulation techniques to remove extranuous white spaces from the
string. When done, print out that temperature, e.g.:
    
    The current temperature showing on the NBC New York weather page is 84°.

        
2.2) Extract from the HTML the brief description of the current
weather conditions found right next to the temperature you extracted
above and print it out. For example:

   The current weather conditions are: Scattered Clouds.

   
2.3) Extract from the HTML the current humidity level and print it
out. For example:

   The current humidity level is 33%.



Hints for Question 2:
====================
    
    Hint 1: The "class" of an HTML element can be very useful when doing
    webscraping. You can use it to help BeautifulSoup find the HTML elements 
    that contain a specific class. Cf. this section of the documentation:
        
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
    
    Notice that, as the documentation makes clear, you must use the argument
    'class_' (ending in an underscore) otherwise you will get an error.
    
    Hint 2: Another very common approach is to search by element ID. Very often
    elements on a web page will have a unique ID which, combined with element type
    (eg, "h2", "a", "span", "li", etc.) easily identify an element on the page. Cf.
    this section of the documentation:
        
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/#the-keyword-arguments
    
"""

# Answer to Question 2.1

# Answer to Question 2.2

# Answer to Question 2.3
