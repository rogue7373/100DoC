#!/usr/bin/python3

# Turn based game for Day 9 of 100 Days of Code Challenge

# Practice with if/else statements 
# Comparison operators: ==, !=, >, <, >=, <=
print("Welcome to the rollercoaster!")
height = int(input("What is yor height in cm? "))

if height >= 120:
    print("You are tall enough to ride the rollercoaster!")
else:
    print("Sorry, you are too short to ride the rollercoaster!")

# True or False segement
# Boolean operators: and, or, not
# Introduction of Modulo  / Odd or Even Code Challenge

print("Welcome to the odd or even number checker!")

number = int(input("Enter your number here to see if it is odd or even. "))

if number % 2 == 0:
    (print("Your number is even"))
else:
    (print("Your number is odd"))
