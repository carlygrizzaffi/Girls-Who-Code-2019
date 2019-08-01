# --- Define your functions below! ---


# --- Put your main program below! ---


def default():
    print("Welcome to Sugars! My name is Jeff.")
def say_default():
    print("Hint: try saying hi")

def say_hello(name):
    print ("Hi,\n" + name)

def location(x):
    print()
    if x == "New York":
        print()

def toppings(y):
    print()
    if y == "yes":
        print()
    elif y == "no":
        print()

def sprinkles(z):
    if z == "yes":
        print()
    elif z == "no":
        print()
        return()

def bye(c):
    if c == "yes":
        print()
        return()
    elif c == "no":
        print ()
        return()

def main():

    default()
    answer = input(" What is your name?")
    say_hello(answer)
    answer = input("What flavor of ice cream would you like?")
    while answer == "chocolate":
        print("Bad choice, choose a new flavor.")
                    #We use else instead of elif because we are not looking for any particular answer
    else:
        print("Wonderful! I will get that for you right away.")
    mylocation = input("Where do you live?")
    location(mylocation)
    mysprinkles = input("Did you know that we offer free sprinkes for any customer in NYC?! Would you like some?")
    sprinkles(sprinkles)
    mytoppings = input("Nice! Would you like any other toppings?")
    toppings(mytoppings)
    mybye = input("Here's your ice cream. Thank You! Have a nice day come back again!")
    bye(mybye)



                    # DON'T TOUCH! Setup code that runs your main() function.

main()
