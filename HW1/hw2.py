# Homework #2

# In all the exercises that follow, insert your code directly in this file
# and immediately after each question.
#
# IMPORTANT NOTE: USE VARIABLES IN ALL YOUR ANSWERS.


""" 

Question 1

You have a stock that closed at $550 on Monday, and then closed at
$560 on Tuesday. Calculate its daily return. The daily return is
defined as the difference in the closing prices, divided by the
closing price the day before.

"""

# Answer to Question 1
close1 = 550
close2 = 560
def dailyReturn(close1,close2):
    ret = (close2 - close1)/close1
    return ret
daily_return = dailyReturn(close1,close2)
print("The daily return is:",daily_return,sep=' ')

"""

Question 2

* Prompt the user to enter their name and save that information in a
variable. 

* Then prompt the user for their age and save that information in a
different variable. 

* Finally, output a sentence indicating the name and age of the user.
Eg, if the user entered 'Juan' and '24', your program should output
"Juan is 24 years old."

"""

# Answer to Question 2
userName = input("Please enter your name: ")
userAge = input("Please enter your age: ")
print("{name} is {age} years old.".format(name = userName, age = userAge))

"""

Question 3

In this exercise you will create a simple financial calculator that
will help the user calculate the future value of a deposit made today.

* Prompt the user for the initial value of the deposit they are making
today and save that in a variable. The value might have decimals,
indicating cents of a dollar. To simplify, assume the user will
neither insert a dollar sign nor use any commas to group zeroes.

* Prompt the user for the yearly interest rate that this deposit will
earn and save that in a variable. To simplify, assume the user will
enter '3' to mean a 3% interest rate or '2.5' to mean a 2.5% interest
rate (ie, without using a percent sign).

* Prompt the user for the number of years during which their deposit
will earn an interest and save that in a variable. Assume the number
of years will be an integer.

* Finally, output the total value of the user's account after interest
has accrued over that number of years.

Expected behavior of your program:

How much is your deposit? 5000
What is the yearly interest rate? 2.5
How many years will be the money be earning interest? 3

After 3 years you will have $5384.45 in your account.

Please do *not* worry if your program displays more than two decimals
when showing the final value of the account.

Note: to answer this question, you will need to 

(i) know -- or find out -- what is the formula to compute the value of
a deposit with an interest rate i over n periods;

(ii) research online how to compute powers (eg, "5 to the power of 3
equals 125") in Python.


"""

# Answer to Question 3
deposit = float(input("Please enter your initial deposit: "))
interest = float(input("Please enter your interest rate: "))
years = int(input("Please enter the number of years of the deposit: "))

def calculate(deposit,interest,years):
    value = deposit * ((interest/100+1)**years)
    return value

value = calculate(deposit,interest,years)
print("The total value of the account is now:", f'{value:.2f}')
