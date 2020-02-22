# Author: Lukas Alatalo

#suppose that someone decides to replace commas with an opening parenthesis ‘(’, 
#and then inserts a closing parenthesis ‘)’ at the end of the sentence. For example, 
#instead of writing ‘Hello, World!’ they write ‘Hello( World!)’. This is done for every comma in the sentence.
#this program takes in a string like this and converts it back into the correct sentence 

#this function takes in a string and a lettter and returns the first
#index where that letter appears in the string.
#if the letter is not in the string, the function returns None.
def find_first(s, letter):
    for i in range(len(s)):
        if s[i]==letter:
            return i
    return None

#this function takes in a string and a letter and returns the last
#index where the letter appears in the string. this is done by iterating
#through the string backwards. If the letter does not appear in the string,
#the function returns None.
def find_last(s, letter):
    for i in range(len(s)-1,-1,-1):
        if s[i]==letter:
            return i
    return None

#this function takes in a string, s, with at least one set of parentheses and replaces the first
#'(' in the string with a comma. The last ')' is also taken away and the new string is returned. 
def get_comma_phrase(s):
    comma = find_first(s,'(')
    s = s[0:comma]+","+s[comma+1:-1]  
    return s                          
        

#This function takes in a string, s, and replaces all '(' with a comma and deletes all ')'.
#This new string is then returned. 
def get_comma_string(s):
    while s[-1] == ')':    #while the last element in the string is ')', we can keep calling get_comma_phrase(s)
        s = get_comma_phrase(s)
    return s
    

s = input("Enter text: ")
print(get_comma_string(s))
