#!/usr/bin/python3

# Data conversion with python

# 1. int()
# 2. float()
# 3. str()
# 4. bool()

# Tip calculator

bill = float(input("What is the bill? "))
service = input("How was the service? ")
split = int(input("How many ways to split? "))

print("Tip amount: ${:.2f}".format(bill * 0.2))
print("Total amount: ${:.2f}".format(bill + (bill * 0.2)))
print("Amount per person: ${:.2f}".format((bill + (bill * 0.2)) / split))
