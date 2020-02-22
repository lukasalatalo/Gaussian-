# Author: Lukas Alatalo
# McGill ID: 260923751
# Assignment 2, Question 3

import random

# Given a dictionary d and value v,
# find and return the key associated with that value.
# (From the slides.)
def reverse_lookup(d, v):
    for key in d:
        if d[key] == v:
            return key
    return None

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`~-=_+[]\{}|;\':",./<>? '
def create_cypher_dictionary(cypher_seed):
    # Note - the following line should remain at the start of this function - do not delete/move it.
    random.seed(cypher_seed) # seed the random number generator with the given seed
    
    cypher = {} # create empty dictionary
    
    #this for loop iterates through every index in LETTERS and creates a key value pair in cypher.
    #a randomly generated number between 00 and 99 is the value to the key and the key is LETTERS at a certain index.
    #the while loop inside checks if the random number is already a value in the dictionary and keeps generating a new
    #number until a unique value is generated.
    for i in range(len(LETTERS)):
        randnum = str(random.randint(0,100))
        if len(randnum)==1:
            randnum = "0"+randnum
        while randnum in cypher.values():
            randnum = str(random.randint(0,100))
            if len(randnum) ==1:
                randnum = "0"+randnum
        cypher[LETTERS[i]] = randnum
        
    return cypher # return the completed cypher dictionary

#this function takes in a string s and the cypher_seed and returns an encrypted version of s.
def encrypt(s, cypher_seed):
    cypher = create_cypher_dictionary(cypher_seed) # get the cypher dictionary
    encrypts=""
    
    #this for loop iterates through each index of s and creates a string with all
    #the values that correspond to the characters at each index of s
    for i in range(len(s)):
        encrypts +=cypher[s[i]]
    s = encrypts
    return s

#this function takes in an encrypted string s and the cypher_seed and returns the decrypted version of s.
def decrypt(s, cypher_seed):
    cypher = create_cypher_dictionary(cypher_seed) # get the cypher dictionary
    decrypts = ""
    for i in range(0,len(s)-1,2):
        if s[i]+s[i+1] in cypher.values():
            decrypts+= reverse_lookup(cypher, s[i]+s[i+1])
    s = decrypts
    return s

#this function takes in a string s, the cypher_seed, and an integer n and encrypts s n times.
def encrypt_multiple_times(s, cypher_seed, n):
    for i in range(n):
        s=encrypt(s,cypher_seed)
    return s

# Source: https://en.wikipedia.org/wiki/Most_common_words_in_English
COMMON_WORDS = [" the ", " be ", " to ", " of ", " and ", " a ", " in ", " that ", " have ", " I ", " it ", " for ", " not ", " on ", " with ", " he ", " as ", " you ", " do ", " at "]

def decrypt_multiple_times(s, cypher_seed):
    cypher = create_cypher_dictionary(cypher_seed) # get the cypher dictionary
    
    loop = True
    
    #This loop keeps calling decrypt(s, cypher_seed) until a common word is found in the decrypted value of s.
    #once a common word is found, the loop stops, and s is returned. 
    while loop == True:
        s=decrypt(s,cypher_seed)
        for i in range(len(COMMON_WORDS)):
            for j in range(len(s)-len(COMMON_WORDS[i])):
                if s[j:j+len(COMMON_WORDS[i])]==COMMON_WORDS[i]:
                    loop = False
    return s
        
        
s = input("Enter text to encrypt: ")
Input = False

#this for loop check if any of the common words is in the string s
#if there is a common word in s, then the input is True.
for i in range(len(COMMON_WORDS)):
    for j in range(len(s)-len(COMMON_WORDS[i])):
        if s[j:j+len(COMMON_WORDS[i])]==COMMON_WORDS[i]:
            Input = True

#if the Input is true and there are common words in s, then the string is encrypted and decrypted.
if Input == True:
    print("Encrypted string:", encrypt(s, 1337))
    print("Decrypted string:", decrypt(encrypt(s, 1337), 1337))

    salted_s = encrypt_multiple_times(s, 1337, 2)
    print("Encrypted string:", salted_s)
    print("Decrypted string:", decrypt_multiple_times(salted_s, 1337))

#if there are no common words in s, then the following is printed.
else:
    print("Invalid input.")
