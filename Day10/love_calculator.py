#!/usr/bin/python3

# User input two names 

first_name = input("Enter your name here? \n ")
second_name = input("Enter your true loves name? \n ")

# Take user input and conver to lower case 
combined_string = first_name + second_name
lower_case_string = combined_string.lower()

# Count the repeating letters in the combined name string
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

# Calculate the love score 
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")



