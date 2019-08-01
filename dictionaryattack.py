#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords

#Take user input for a password.
passwords  = []
with open("dictionary.txt") as f:
    for line in f:
       passwords.append(line.split())


#Write logic to see if the password is in the dictionary file below here:
for password in passwords:
    y = input("Please type a password: ")
    if y.split() in passwords:
        print("Your password is not secure")
    else:
        print("Good password!")

#Explain how your program should work when a user enters a password that is susceptible vs a strong password.

#Accurately use a loop in Python.
