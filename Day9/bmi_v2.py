#!/usr/bin/python3

# Variables for collection user data. 

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

height_as_float = float(height)
weight_as_int = int(weight)

# Using the exponent operator ** 

bmi = weight_as_int / height_as_float ** 2

# or using multiplicaiton and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print("Your calculated BMI is: " + str(bmi_as_int))

if bmi_as_int < 18.5:
    print("You are underweight")
elif bmi_as_int < 25:
    print("You are normal weight")
elif bmi_as_int < 30:
    print("You are overweight")
elif bmi_as_int < 35:
    print("You are obese")
