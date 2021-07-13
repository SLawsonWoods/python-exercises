# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## 1a prompt the user for a day of the week, print out whether the day is Monday or not
user_input = input ("Please enter a day of the week.")
user_input
if user_input == "Monday":
    print("Today is Monday")
else:
    print("Today is NOT Monday")
#%%
## 1b prompt the user for a day of the week, print out whether the day is a weekday or a weekend

weekend_or_weekday = input ('Please enter a day of the week.')
weekend_or_weekday
if weekend_or_weekday == "Saturday" or weekend_or_weekday == "Sunday":
    print("It's the weekend.")
else:
    print("Turn on workmode.")
#%%
## 1c create variables and make up values for the number of hours worked in one week;the hourly rate; how much the week's paycheck will 
hours_worked_weekly = 58
hourly_rate = 60
overtime = hours_worked_weekly - 40
paycheck_weekly = (hours_worked_weekly * hourly_rate) + (overtime *(hourly_rate * 1.5))
print(paycheck_weekly)
#%%
## Loop Basics a.While
## Create an integer variable i with a value of 5.
## Create a while loop that runs so long as i is less than or equal to 15
## Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1
#%%
## Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2
#%%
## Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5
#%%
i = 2
while i < 1000000:
    print(i)
    i **= 2
#%%
## Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5

#%%
## b. i. Write a loop that uses print to create the output shown below.
##7 x 1 = 7
##7 x 2 = 14
##7 x 3 = 21

user_input1 = int(input("Please enter a number"))
for num in range(0,10):
    print(f'{user_input1} X {num + 1} =  {user_input1 * (num + 1)}')
    num += 1

#%% 
##Create a for loop that uses print to create the output shown below.
##1
##22
##333
##4444

for n in range(1, 10):
    print(str(n)* n)
 #%%
## c. break and continue
## Prompt the user for an odd number between 1 and 50. Use a loop and a break 
## statement to continue prompting the user if they enter invalid input. 
##(Hint: use the isdigit method on strings to determine this). Use a loop and 
## the continue statement to output all the odd numbers between 1 and 50, 
## except for the number the user entered.
## Your output should look like this:
## Number to skip is: 27
## Here is an odd number: 1
## Here is an odd number: 3
#%%
## d. Prompt the user to enter a positive number and write a loop that counts 
## from 0 to that number. 

num_selected = int(input('Please enter a positive number.'))
n = 0
for n in range(num_selected + 1):
    print(n)
    n += 1
#%%
## e Write a program that prompts the user for a positive integer. Next 
## write a loop that prints out the numbers from the number the user entered 
## down to 1.
user_input2 = int(input('Please enter a postive whole number.'))
n = user_input2
for n in range(user_input2,0,-1):
    print(n)
    n -= 1
#%%
## 3 Fizzbuzz
## Write a program that prints the numbers from 1 to 100.

for n in range(1,101):
    print(n)
    n += 1
#%%
## For multiples of three print "Fizz" instead of the number
for n in range(1,101):
    print(n)
    n += 1
    if n % 3 == 0:
        print("Fizz")
#%%
## For the multiples of five print "Buzz".

for n in range(1,101):
    print(n)
    n += 1
    if n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
#%%
## For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1,101):
    print(n)
    n += 1
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
#%%
## 4 Display a table of powers.
## Prompt the user to enter an integer.

user_input3 = int(input("Please enter a whole number."))

## Display a table of squares and cubes from 1 to the value entered.
    
        