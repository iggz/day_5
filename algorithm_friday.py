# Friday, April 19

# Whiteboarding/Psuedocoding/talking through a problem/explaining your code/
# coming up with solutions together!

# Remember, we're all at different experience levels, so start with a couple of the 
# "warm up" problems so everyone can participate; don't just jump on the last 3! :D

# TRY to stay away from built-in methods like count() sort() replace() ord() etc, for now...

# 1
# write a function that counts the appearance of a letter within a string.
# casing should NOT matter.

# single_letter_count("Hello World", "h") # 1
# single_letter_count("Hello World", "z") # 0
# single_letter_count("HelLo World", "l") # 3

string1 = "hello world"

for index in string1:
    print (index)


#define single_letter_count below:
# from random import shuffle
# def single_letter_count(string, letter):
#    pass

# 2
# this function takes in a string and returns a dictionary with letters and
# their count in the string.
# multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}

# flesh out multiple_letter count:

def multiple_letter_count(str):
    pass

# challenge: count vowels only!, or try a sentence and discount spaces

# 3
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
# so "a" is considered a different type of stone from "A".

# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# feel free to change these variables below
#j = 'aA'
#s = 'aAAbbbb'

def num_jewels_in_stones(jewels, stones):
    pass


# 4
# write a function that accepts a string and tests if it is a palindrome
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
# is_palindrome('amanaplanacanalpanama') # True

# input_string = input("Enter a word: ")
# def is_palindrome(str):
#     lower_string = str.lower()
#     start_counter = 0
#     end_counter = len(lower_string)-1
#     while start_counter < end_counter:
#         if lower_string[start_counter] != lower_string[end_counter]:
#             return False
#         elif lower_string[start_counter] == lower_string[end_counter]:
#             start_counter += 1
#             end_counter -= 1
#     return True

# print(is_palindrome(input_string))


# 5
# write a function that accepts a list and a search term and returns the number
# of times the search term appears in the list
# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1

def frequency(list, letter):
    pass 


# 6
# write a function that accepts a list of numbers and returns the product of all
# even numbers of list
# multiply_even_numbers([2,3,4,5,6]) # 48

def multiply_even_numbers(list):
    pass


# 7
# write a function that accepts a string and returns the same string with the
# first letter capitalized. perhaps use slices to help you out! DON'T use .capitalize()
# capitalize("tim") # "Tim"
# capitalize("matt") # "Matt"

def capitalize(string):
    pass


# 8
# total sum of all numbers divisible by 3 or 5 < 1000

def sum_odds_by_three_five(int):
    pass


# 9
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def sum_even_fib():
    fibo = [1, 2]
    n = len(fibo)
    result = 2
    while fibo[n - 1] < 4000000:
        fibo.append((fibo[n -1]) + (fibo[n -2]))
        n = len(fibo)
        print(fibo)
        if fibo[n -1] % 2 == 0:
            result += fibo[n -1]
            print(result)
sum_even_fib()


# 10
# Write a function called average_pair. given a list of SORTED (ie: 1,2,3) integers and a target avg, 
# determine if there is a pair of values in the array where the average of the pair equals the target avg.
# There may be more than one pair that matched the target avg.

# examples:
# average_pair([1,2,3]. 2.5) returns TRUE
# average_pair([-1,0,3,4,5,6], 4.1) returns FALSE

def average_pair(list, avg):
    pass


# 11
# Write a function which returns a generator that will yield and unlimited number of primes, 
# starting from the first prime, which is 2
# primes = next_prime()
# [next(primes) for i in range(25)]
# # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def next_prime():
    pass