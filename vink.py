# Author: Lukas Alatalo
# McGill ID: 260923751
# Assignment 1, Question 4

def vink_sequence(n,k,j): # the parameters of this function are the user inputs for n, k, and j.
    # Your code here.
    sum = 1  #sum is the counter for how many terms it takes to get to 1. 
    for i in range(j): #the for loop is run j number of times.
        if n==1:  #this if statement checks whether the sequence has gotten to 1 and breaks the loop if it has.
            break
        #the following conditional statements check if n is even or odd and performs the correct calculations.
        elif n%2 == 0: 
            n = n/2
            sum = sum +1  
        else:
            n = 3*n + k
            sum  = sum + 1
    if n!=1: #if the sequence does not reach 1, the ouput is -1.
        sum = -1
    print(sum)

# Your code here.

#Asking for user inputs and turning them into integer types.
n = int(input("Enter n: "))
k = int(input("Enter k: "))
j = int(input("Enter j: "))

#This if statement checks whether the input was valid or not.
if n<=0 or k<0 or j<=0:  
    print("Invalid input.")
else:  #if the inputs are valid, the function is called.
    vink_sequence(n,k,j)