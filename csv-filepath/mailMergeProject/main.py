#TODO: Create a letter using starting_letter.txt

with open("Input/Names/invited_names.txt", mode="r") as names:
    invitedNames = names.readlines() #store invited names into a list using readlines

for name in invitedNames:
    new_name = name.replace(" ", "") # if name has any spaces, remove them for easier file navigation
    filepath = f"Output/ReadyToSend/{new_name}.txt"  # output has an error where name\n
    newFilepath = filepath.replace("\n", "") # fix \n error by replacing it
    with open(newFilepath, mode = 'w') as names: # write to file, if it doesn't exist create it
        new_name = name.strip() # name will make comma go to next line for some reason, use strip to remove special char
        content = names.write(f"Dear {new_name},\n\n" # weird how we have to give it a variable to write in a file
            "You are invited to my birthday this Saturday.\n\n"
            "Hope you can make it!\n\n"
            "Andrew")


#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp