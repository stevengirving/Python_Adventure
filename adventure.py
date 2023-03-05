from sys import exit
from random import randint

""" A short text-based adventure game to explore the use of functions,
    lists, user input, and other shenanigans. 
"""

def main_menu():
    """ Prints the main menu of the game to allow exit"""
    print("""
MAIN MENU

    > NEW GAME
    > EXIT

TYPE SELECTION:
"""
    )
    show_options = ["New Game", "Exit"]
    selection = user_input(show_options)
    if selection.lower() == "new game":
        pass
    else:
        dead("Thank you for playing!")

def difficulty():
    """Sets the amount of health the player has"""
    print("Please choose your difficulty:")
    show_options = ["Easy", "Medium", "Hard"]
    selection = option_generator(show_options)
    if selection.lower() == "easy":
        return 20
    elif selection.lower() == "medium":
        return 15
    else:
        return 10

def option_generator(options):
    """Prints a vertical list of options in all caps"""
    print("\n")
    for i in options:
        print("> ", i.upper())
    print("\n")
    selection = user_input(options)
    return selection

def user_input(options):
    """ Loops user to re-type their answer to match options"""
    loop = True
    while loop is True:
        user_says = input("> ")
        loop = verify_input(user_says, options)
    return user_says

def start():
    """ Initiates the start of the game"""
    print("Hello! Welcome to this little adventure!")
    print("\nWhat is your name?\n")
    player_name = input("> ")
#    player_name = confirm_player_name(input("> "))
    print(f"\nWell {player_name}, let's get started.")
    return player_name

'''
def confirm_player_name(name):
    loop = True
    while loop is True:
        print(f"You wrote {name}, is this correct?")
        options = ["Yes", "No"]
        confirm = user_input(options)
        if confirm == "yes":
            pass
        elif confirm == "no":
            name = input("> ")
            confirm_player_name(name)
    return name
'''

def update_inventory(item, action):
    """System to add or remove items to the inventory list"""
    if action == "add":
       inventory.append(item)
    elif action == "remove":
       inventory.remove(item)
    else:
       dead("Something messed up with update_inventory")

def finish_room(room):
    """Marks a room as "completed" to allow unique or alternate text"""
    completed_rooms.append(room)

def verify_input(user_input, options):
    """Checks the user's input against available options"""
    cleaned_options = []
    for option_cleaner in options:
        cleaned_options.append(option_cleaner.lower())
    if user_input.lower() in cleaned_options:
        print("\n")
        return False
    else:
        print("Please choose one of the options.\n")
        return True

def house_front():
    """Describes the front of The House and available actions"""
    current_room = house_front
    if current_room in completed_rooms:
        pass
    else:
        print("""
    You are out on a walk one day when you come across a house you
    have never seen before. Oddly enoguh, you don't even recognize
    the neighbourhood you're in. You take a closer look at the house.
    """
        )
        finish_room(current_room)
    print("""
    The house itself seems to be abandoned, at least you cannot 
    see any lights on. The front door lays open, though perhaps
    the owner simply forgot it open while doing yardwork? They
    could be in the backyard, why not check. Though the front door
    is awfully inviting...   
    """
    )
    show_options = ["Go inside", "Go to back", "Leave"]
    selection = option_generator(show_options)
    if selection.lower() == "go inside":
        print("Going inside!")
        pass
    elif selection.lower() == "go to back":
        print("Going around to the back!")
        pass
    else:
        print("Getting the heck outta here!")
        house_leave()

def house_behind():
    """Describes behind The House and available actions"""
# -> Look through windows - 3 choices
# -> Go back to front of house

def house_entrance():
    """Describes the first room of The House and available actions"""
# -> Left Door
# -> Right Door
# -> Entrance door, now locked

def house_left():
    """Describes the Left Room of The House and available actions"""
# Some sort of puzzle
# Door locked until solved
# Secret item?
# -> House Back
# -> House Entrance

def house_right():
    """Describes the Right Room and summons the Bear fight"""
    current_room = house_right
    if current_room in completed_rooms:
        pass
    else:
        print("This will be the introductory message to the room")
        print("Now summoning.... THE BEAR")
        summon_bear(10, False)
        finish_room(current_room)
    
    print("This should be a generic message post-Bear fight")

def summon_bear(bear_health, bear_defeated):
    if bear_defeated is False:
        print(f"Current HP: {health}")
        show_options("Fight", "Defend")
        selection = option_generator(show_options)
        if selection.lower() == "fight":
            print("You go in for a fight!")
            bear_health -= 3
        elif selection.lower() == "defend":
            print("You try to defend yourself against a bear. It hurts.")
            health -= 2

# Actually could do a simple fight system: (NEW FUNCTION???)
#   Bear has 15? HP
#   Player has {health}  HP
#   FIGHT (-3 bear HP) | DEFEND (-2 user HP) maybe ATK//2?
#   BEAR does -5 HP per hit?
#       Maybe 1/3 chance attack, 2/3 chance nothing
#       This would mean death in 4/3/2 rounds...

# Secret item!
# -> House Back
# -> House Entrance

def house_back():
    """Descibes the Back Room of The House and available actions"""
# THE FINAL PUZZLE!!!
# IT'S JUST GONNA BE FUCKING SODOKU
# THAT'S A LIE
# If both secret items:
# -> House Secret

def house_secret():
    """Describes the SECRET ROOM of The House, needs keys!"""
# Idea: Collect item from Left and Right to find
# Why? For fun!
# Some secret message or something! idk!

# Try to Leave
# TODO 

def house_leave():
    """Runs a small loop of getting "lost" the first time, then allows
    exit"""
    current_room = "house_leave"
    if current_room in completed_rooms:
        print("You actually have your bears now, and don't know how you got lost before.")
        return
    else:
        loop = True
    print("Generic description of the neighbourhood")

    while loop is True:
        for i in range(0,5):
            print("Repetitive description.")
            input("> ")
            if i == 5:
                break
        loop = False
    finish_room(current_room)
    house_front()

        
# Loop x5 message of walking if loop is False
# Return to start
# set loop is True
# Describe actual exit avoiding loop
# exit(0)

# Game Over Message
def dead(why):
    """ Prints the game over message and exits"""
    print(f"{why} Game over!")
    exit(0)
    
room_list = ["house_front", "house_behind", "house_leave", "house_entrance," "house_left", "house_right", "house_final", "house_secret"]
inventory = []
completed_rooms = []
main_menu()
health = difficulty()
print("Your starting health will be:", health, "HP\n")
player_name = start()
house_front()

if inventory == []:
    inventory.append("Nothing")
else:
    pass

print("Congratulations {}! You left the neighbourhood with \
{} HP! Here's what you had in your pockets: {}".format(player_name, health, *inventory))
