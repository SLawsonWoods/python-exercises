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
## 1b prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# weekend_or_weekday = input ('Please enter a day of the week.')
# weekend_or_weekday
# if weekend_or_weekday == "Saturday" or weekend_or_weekday == "Sunday":
#     print("It's the weekend.")
# else:
#     print("Turn on workmode.")

## 1c create variables and make up values for the number of hours worked in one week;the hourly rate; how much the week's paycheck will be.

# hours_worked_weekly = 58
# hourly_rate = 60
# paycheck_weekly = hours_worked_weekly * hourly_rate
# print(paycheck_weekly)

## Loop BasicsWhile
## Create an integer variable i with a value of 5.
## Create a while loop that runs so long as i is less than or equal to 15
## Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1
## Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 5
while i <= 100:
    print(i)
    i += 2
## Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5
#%%
i = 2
while i < 1000000:
    print(i)
    i ** 2
#%%
