# Homework #5

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
# @author: Harry Zhang
"""

Question 2

Below you will find a list of product prices in USD below (prices_usd).

2.1) Create a new empty list called prices_brl.

2.2) Use a for loop to populate the newly created list prices_brl
with the same prices, but converted into Brazilian real. (As of Feb
28th, the exchange rate is approximately 1 USD = 3.74 BRL.) 

2.3) Modify the original list prices_usd so that it contains the
*rounded* prices. (The prices can be stored either as int or float,
but must not have decimal values.)

2.4) Modify the list prices_usd so that the prices are sorted from the
highest to the lowest.

"""

prices_usd = [48.8, 28.9, 58.4, 51.0, 98.0, 75.7, 14.8]


# Answer to Question 2.1
prices_brl = []
# Answer to Question 2.2
for i in prices_usd:
    prices_brl.append(i * 3.74)
print(prices_brl)
# Answer to Question 2.3
for i in range(len(prices_usd)):
    prices_usd[i] = round(prices_usd[i])
print(prices_usd)
# Answer to Question 2.4
prices_usd.sort(reverse = True)
print(prices_usd)
