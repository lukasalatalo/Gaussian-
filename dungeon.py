# Author: Lukas Alatalo 
# McGill ID: 260923751
# Assignment 2, Question 4

AUTHOR = "Lukas Alatalo"
ROOM_NAME = "Piano Man"

def escape_room():
    print(
        '''You find yourself in a room with a piano, a matress, and a bulletproof window.
There is a door that is locked and cannot be openned with a key. You can examine the window,
the mattress and the piano. There is also a Keymaster called Lukas who can give you a hint.
Find a way to get out.''')

    commands = {
        # insert key-value pairs here
        "examine piano" : "The piano is fully functional. The word 'glass' is faintly carved into the piano.",
        "examine window" : "Looking closely at the window, you can see in writing, 'press first key from the right'.",
        "examine mattress" : "The mattress is very comfy but unfortunately yields no clues.",
        "talk to lukas" : "Here is your hint: the piano is the key to it all." , 
    }
    
    #this loop keeps running until the user enters that correct command and True is returned.
    while True:
        cmd = input("> ")
        cmd = cmd.lower()
        
        if cmd == ("press first key") or cmd ==("play first key") or cmd ==("press first key from the right") or cmd ==("play first key from the right"):
            print("Congrats! The door is now open and you have escaped!")
            return True
        elif cmd == "commands":
            print("Commands are: examine piano, examine window, examine mattress, talk to lukas")
        elif cmd in commands:
            print(commands[cmd])
        else:
            print("Invalid input.")
        
        

# Calling the function so that it runs when we run the file.
escape_room()