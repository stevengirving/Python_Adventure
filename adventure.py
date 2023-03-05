from sys import exit
""" A short text-based adventure game to explore the use of functions,
    lists, user input, and other shenanigans. 
"""

# Adventure design!

# Main Menu
def main_menu():
    """ Prints the main menu of the game to allow exit"""
    print("""MAIN MENU

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
    """Sets the amount of mistakes player can make"""
    print("Please choose your difficulty:")
    show_options = ["Easy", "Medium", "Hard"]
    selection = option_generator(show_options)
    if selection.lower() == "easy":
        return 5
    elif selection.lower() == "medium":
        return 3
    else:
        return 1

def option_generator(options):
    for i in options:
        print("> ", i.upper())
    selection = user_input(options)
    return selection

def user_input(options):
    """ Loops user to re-type their answer to match options"""
    loop = True
    while loop is True:
        user_says = input("> ")
        loop = verify_input(user_says, options)
    return user_says

# Start message welcoming the player
def start():
    """ Initiates the start of the game"""
    print("Hello! Welcome to this little adventure!")
    player_name = get_player_name()
    print(f"{player_name}, let's get started.")
    return player_name

# Define player name
def get_player_name():
    """ Collects the player's name"""
    print("What is your name?")
    return input("> ")

# Inventory system to add or remove
def update_inventory(item, action):
   if action == "add":
       inventory.append(item)
   elif action == "remove":
       inventory.remove(item)
   else:
       dead("Something messed up with update_inventory")

def finish_room(room):
    completed_rooms.append(room)

# Takes user input, verifies it against the options
def verify_input(user_input, options):
    cleaned_options = []
    for option_cleaner in options:
        cleaned_options.append(option_cleaner.lower())
    if user_input.lower() in cleaned_options:
        return False
    else:
        print("Please choose one of the options.")
        return True

# Front of House
def house_front():
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
        finish_room("house_front")
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
        pass

    player_action(current_room, selection)

# Back of House
# -> Look through windows - 3 choices
# -> Go back to front of house

# House Entrance
# -> Left Door
# -> Right Door
# -> Entrance door, now locked

# House Left
# Some sort of puzzle
# Door locked until solved
# Secret item?
# -> House Final
# -> House Entrance

# House Right
# Puzzle!! Fight??? BEARS?
# Secret item!
# -> House Back
# -> House Entrance

# House Final
# THE FINAL PUZZLE!!!
# IT'S JUST GONNA BE FUCKING SODOKU
# THAT'S A LIE
# If both secret items:
# -> House Secret

# House... Secret????
# Idea: Collect item from Left and Right to find
# Why? For fun!
# Some secret message or something! idk!

# Utilize if-elif-else for player actions
# Uses the current_room as a way 
def player_action(current_room, next_room):
    dead("You've reached the current end!")

# Try to Leave
# TODO 
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
    
room_list = ["house_front", "house_back", "house_leave", "house_entrance," "house_left", "house_right", "house_final", "house_secret"]
inventory = []
completed_rooms = []
main_menu()
health = difficulty()
print(health)
player_name = start()
house_front()
