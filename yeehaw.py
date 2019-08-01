def is_valid_input(answer):
    yes = ["yeah", "yeehaw", "yes", "ya", "Y", "y"]
    no = ["no", "nah", "NTY"]
    if answer in yes:
        return(True)
    elif answer in no:
        return(False)
    else:
        return("Error")

pineapple = input("Do you like pineapple?")

if is_valid_input(pineapple) == True:
    print("Spongebob Squarepants")
elif is_valid_input(pineapple) == False:
    print("Mr. Krabs")
else: print("Sorry I don't know what that means")
