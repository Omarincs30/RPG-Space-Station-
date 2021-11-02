# Omar Diaa Abdelhaleem Abdullat
# Computer Science 30
# October 22, 2021 (Modified November 2)
# RPG Simple menu


# Introduction and rules.
def menu():
    print("Welcome to Omar's Spaceship game, where you explore a spaceship")
    print("Remeber that all answers must start with a captial letter")
    print('''let's get started by completing one of the
    following actions: Go Exploring, Go Flying, Go Cooking, or Quit.''')
    while True:
        choice = input("Action:")
# The First Choice starts here.
        if choice == "Go Exploring":
            print("You explore around and you find 2 doors, door 1 and 2")
            Exploring = input("Do you go into door 1 or 2?")
            if Exploring == "1":
                print("You go in and you find an octupus in a cage!")
            elif Exploring == "2":
                print("You go in and find a room full of guns!")
            elif Exploring == "Quit":
                print("Goodbye.")
                break
            else:
                print("Please input a valid answer.")
# The Second choice starts here.
        elif choice == ("Go Flying"):
            print("You go into the cockpit")
            Flying = input("Do you want to be the pilot or navigator?")
            if Flying == "Pilot":
                print("You are now in full control of the space ship.")
            elif Flying == "Navigator":
                print("You are now the Navigator")
            elif Flying == "Quit":
                print("Goodbye.")
                break
            else:
                print("Please input a valid answer.")
# The last choice starts here.
        elif choice == ("Go Cooking"):
            print("You go into the kitchen")
            Cooking = input("Do you want to cook a salad or a hamburger?")
            if Cooking == "Salad":
                print("You cook a salad for the whole crew")
            elif Cooking == "Hamburger":
                print("You cook some hamburgers for the whole crew")
            elif Cooking == "Quit":
                print("Goodbye.")
                break
            else:
                print("Please input a valid answer.")
# Quit Function and the invalid answer function.
        elif choice == "Quit":
            print("Goodbye.")
            break
        else:
            print("Please input a valid answer.")
