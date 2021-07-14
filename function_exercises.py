#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 09:25:43 2021

@author: sarahwoods
"""
#%%
## 1. Define a function named is_two. It should accept one input and return True 
## if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == "2" or x == 2:
        return True
    else:
        return False
x = 3
print(is_two(x))
#%%
## 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(y):
    for o in y:
        if o in ('aeiou'):
            return True
    else:
        return False
y = 'lkd'
print(is_vowel(y))
#%%
## 3. Define a function named is_consonant. It should return True if the passed 
## string is a consonant, False otherwise. Use your is_vowel function to 
## accomplish this.

def is_consonant(value):
    for v in value:
        if v not in ('aeiou'):
            return True
        else:
            return False
value = 'lala'
print(is_consonant(value))
#%%
## 4. Define a function that accepts a string that is a word. The function 
##should capitalize the first letter of the word if the word starts with a consonant.

def starts_with_upper(word):
        if word[0] not in ('aeiou'):
            return word.capitalize()
        else:
            return word
word = 'lala'
print(starts_with_upper(word))
#%%
## 5. Define a function named calculate_tip. It should accept a tip percentage 
## (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(bill, tip_rate):
    total = bill * tip_rate 
    return total
bill = 10
tip_rate = .10
print(calculate_tip(bill, tip_rate))
#%%
## 6. Define a function named apply_discount. It should accept a original 
## price, and a discount percentage, and return the price after the discount 
## is applied.

def apply_discount(sticker_price, discount_value):
    sticker_priice = 10
    discount_value = .25
    total = (sticker_price * discount_value)
    
    
    