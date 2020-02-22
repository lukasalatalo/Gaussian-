# Author: Lukas Alatalo
#This program calculates the radius, surface area, or the volume of a sphere based on user inputs.

import math

data = input("What piece of data do you have? ")  #Asking the user to input the piece of data that they have.

#The following if, elif, and else statements performs calculations based on the user's piece of data.
#If the user inputs a valid piece of data, the value of that data is asked for, turned into a float, and stored in num.
#If the user's input is valid, the radius, volume, and surface area are calculated in terms of the given data
#and printed to the screen. 
if data == "radius":
    num = float(input("Enter the number: "))
    if num<0:
        print("Invalid input.")
    else:
        print("You entered", num,"for the radius.")
        vol = str(4/3*math.pi*num**3)         #volume in terms of radius 
        area = str(4*math.pi*num**2)          #surface area in terms of radius.
        print("The volume is", vol,"and the surface area is", area+".")

elif data == "surface area":
    num = float(input("Enter the number: "))
    if num<0:
        print("Invalid input.")
    else:
        print("You entered", num,"for the surface area.")
        rad = str((num/(4*math.pi))**(1/2))          #radius in terms of surface area.
        vol = str(4/3*math.pi*(num/(4*math.pi))**(3/2))     #volume in terms of surface area.
        print("The radius is",rad,"and the volume is",vol+".")

elif data == "volume":
    num = float(input("Enter the number: "))
    if num<0:
        print("Invalid input.")
    else:
        print("You entered", num,"for the volume.")
        rad = str((3*num/(4*math.pi))**(1/3))          #radius in terms of volume
        area = str(4*math.pi*(3*num/(4*math.pi))**(2/3))   #surface area in terms of volume.
        print("The radius is", rad,"and the surface area is", area +".")

else: 
    print("Invalid input.")
