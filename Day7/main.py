#!/usr/bin/python

# Don't change the code below. 

height = input("Enter your height in m: ")

weight = input("Enter your weight in kg: ")

# Don't chage the code above 

height_as_float = float(height)
weight_as_int = int(weight)

# Using the exponent operator ** 

bmi = weight_as_int / height_as_float ** 2

# or using multiplicaiton and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print("Your calculated BMI is: " + str(bmi_as_int))




