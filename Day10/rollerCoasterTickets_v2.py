#!/usr/bin/python3

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You are tall enough to ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age <= 45 and age <= 55:
        # Added a free ride for those experiencing a mid life crisis. The above elif statement will break out of the elif loop and return the free ride message. It is of note, the rider will still need to pay for any photos.
        print("Everthing is going to be ok. Have a free ride on us!")
    else:
        bill = 12 
        print("Adult tickets are $12.")

    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else: 
    print("Sorry, you are too short to ride the rollercoaster!")
