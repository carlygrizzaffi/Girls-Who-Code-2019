# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decide to go left and you arrive in a dark, dingy dungeon. You see a dim light shining before you and a sign is lying beside it. It reads... Go towards the light. Follow the path before the darkness eats you alive. You must decide again: you would you like to go towards the light or stay where you are? \n :]")
    # Update to match your story.
user_input = input("Type either 'towards the light' or 'stay'")
if user_input == "towards the light" :
    print ("You escape the dugeon and arrive in a beautiful castle. Would you like to explore or stay where you are? \n :]")
elif user_input == "stay":
    print ("monsters eat you in the darkness \n :]")
    # Continue code to finish story.
user_input = input("Type either 'stay' or 'explore'")
if user_input == "stay":
    print("Congratulations! You are the new resident of the castle. Enjoy your stay! \n :]")
elif user_input == "explore":
    print("The guards see you wandering and arrest you due to your suspicious action. They throw you in the moat and tell you to never return. \n :]")

if user_input == "right":
    print("You choose to go right and you hear waves and birds chirping. Would you like to stay where you are or go towards the sound.")
    # Update to match your story.
    user_input = input("Type either 'stay' or 'towards the sound'")
if user_input == "stay":
    print("You live a happy life at the beach! Enjoy! \n :]")
elif user_input == "towards the sound" :
    print("You meet a friendly sea lion. Your new friend walks you home. You arrive safely. \n :]")
    # Continue code to finish story.
