# Author: Lukas Alatalo
#this program calculates the output of the guasian function based on user inputs.

import math

def gaussian_2D(x,y,A,xO,yO,sigmaX,sigmaY): # parameters are defined by the user inputs
    # Your code here.
    print(A*math.exp(-((x-xO)**2/(2*sigmaX**2)+(y-yO)**2/(2*sigmaY**2))))  #printing the calculation of the gaussian function using the parameters. 
    
# Your code here.

#Asking for user inputs and turning those inputs into floats.
x = float(input("Enter value for x: "))    #
y = float(input("Enter value for y: "))
A = float(input("Enter value for A: "))
xO = float(input("Enter value for xO: "))
yO = float(input("Enter value for yO: "))
sigmaX = float(input("Enter value for sigmaX: "))
sigmaY = float(input("Enter value for sigmaY: "))

#Calling the function.
gaussian_2D(x,y,A,xO,yO,sigmaX,sigmaY)
