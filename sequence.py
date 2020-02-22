# Author: Lukas Alatalo
# McGill ID: 260923751
# Assignment 2, Question 1

#this function takes in a list of integers and returns the smalles integer not in the list.
def fetch(numbers):
    #if the user only inputs 'done', the function returns 1.
    if numbers==True:
        return 1
    else:
        numbers.sort()
        if numbers[0]==0: #if the user inputs 0, the function returns 1.
            return 1
        elif numbers[0] != 1: #if the smallest integer in the list is not 1, the function returns 1.
            return 1
        else:
            #this for loop iterates from the second integer in the list through to the last.
            for i in range(1,len(numbers)):
                if numbers[i]-1 == numbers[i-1]:
                    if i ==len(numbers)-1:
                        return numbers[i]+1
                    if numbers[i]+1!=numbers[i+1]:
                        return numbers[i]+1
                elif numbers[i]-1==0:
                    continue 
                else:
                    return numbers[i]-1
            return numbers[len(numbers)-1]+1

#this function returns a list of integers from a user's inputs.
def get_list_from_input():
    Input = input("Enter number(s): ")        
    numbers = []
    if Input == "done":
        return True
    
    #until the user enters done, this loop keeps repeating, adding integers to the list.
    while Input != "done":
        comma = []
        #this loop iterates through the input and checks if there are commas.
        #if there are commas, the index of the comma is appended to the list commas.
        for i in range (len(Input)):
            if Input[i] == ",":
                comma.append(i)
                
        #if there are no commas in the input, the integer is appended to the numbers list.
        if len(comma)==0:
            numbers.append(int(Input))
            
        #if there are commas, the integers inbetween the commas are appended the the numbers list.
        else:
            numbers.append(int(Input[0:comma[0]]))
            numbers.append(int(Input[comma[-1]+1:len(Input)]))
            for i in range(len(comma)-1):
                numbers.append(int(Input[comma[i]+1:comma[i+1]]))
                
        Input = input("Enter number(s): ")
    return numbers

numbers = get_list_from_input()
print(fetch(numbers))


