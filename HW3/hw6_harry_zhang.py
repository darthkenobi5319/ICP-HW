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

In Python, you can tell your program to wait for n seconds by writing
the following two statements:

import time
time.sleep(n)

Create a variable called seconds_elapsed and set it to zero. Using a
while loop, write a program that prints out a message every second
until 5 seconds have gone by:

1 seconds have elapsed
2 seconds have elapsed
3 seconds have elapsed
4 seconds have elapsed
5 seconds have elapsed
Done!

Note: Do not worry about fixing the broken grammar of "1 seconds have elapsed".

"""

# Answer to Question 1
import time
seconds_elapsed = 0
while seconds_elapsed < 5:
    time.sleep(1)
    seconds_elapsed += 1
    print("%d seconds have elapsed" % seconds_elapsed)
print("Done!")
"""

Question 2

Although for loops provide a more "natural" way to iterate over the
elements of a list, while loops can also be used to do that. 

2.1) Write code that uses a while loop to iterate over the 6 prices in
list 'prices' and computes the average price. 

2.2) Rewrite your answer to Question 2.1 so that, using the len()
function to obtain the number of elements in the list, your code now
successfully computes the average price for a list of *any length*.
That is, your code should _not_ assume that the list 'prices' has just
6 elements.

"""
prices = [843.1, 859.9, 588.5, 906.4, 869.7, 1010.2]
# Answer to Question 2
i = 0
total_price = 0
while i < len(prices):
    total_price += prices[i]
    i += 1
average_price = total_price/i
print(average_price)   
    


"""

Question 3

This question asks you to write an if-elif-else statements. All
conditions that you need to write depend only on the values of the
variables defined below: you do not need to define any variables.

To make sure your code is correct, experiment with setting the
variables to different values and checking if you get the desired
behavior.

There are countless ways in which this can be answered. If unsure if
your answer is correct, just experiment with different values. If your
code does what it should, then it is correct!

Write code that prints out:
    
a) "the weather doesn't suck today and last week was good to me" if
the weather is not sucky today and you (EITHER went on 5 or more dates
last week OR went to the gym 3 or more times)

b) "though last week wasn't great, at least the sun is shining" if the
condition in (a) is not True but it is sunny today 

c) "well, at least I am going to the Met..." if the condition in (a)
is not True, it is not sunny today but you plan to go to the Met

d) "hey, things suck right now but I can at least ride the subway
twice" if the condition in (a) is not True, it is not sunny today, you
don't plan to go to the Met but your bank_balance is at least twice
the price_of_a_subway_ride. (Note: use the variable
price_of_a_subway_ride in your answer, not the value 2.75.)

e) "listen, can you at least lend me $10?" if none of the above apply

"""

weather_today        = "sunny"   # string, describes the weather today, can take the values "sunny", "sucky", "snowy", "rainy"
dates_past_week      = 3         # integer, number of dates you went on the last week
going_to_the_met     = True      # boolean, True or False
exercized_past_week  = 4         # integer, number of times you exercized last week
bank_balance         = 200.85    # float, your bank balance today in USD
price_of_subway_ride = 2.75      # float, current price of a subway ride

# Answer to Question 3
if weather_today != "sucky" and (dates_past_week >= 5 or exercized_past_week >= 3):
    print("the weather doesn't suck today and last week was good to me")
elif weather_today == "sunny":
    print("though last week wasn't great, at least the sun is shining")
elif going_to_the_met == True:
    print("well, at least I am going to the Met...")
elif bank_balance >= (2 * price_of_subway_ride):
    print("hey, things suck right now but I can at least ride the subway twice")
else:
    print( "listen, can you at least lend me $10?")