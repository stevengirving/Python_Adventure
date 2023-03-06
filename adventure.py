from sys import exit
from random import randint

""" A short text-based adventure game to explore the use of functions,
    lists, user input, and other shenanigans. 
"""

player_health = 25

def main_menu():
    """Prints the main menu of the game to allow exit"""
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
        return 5
    elif selection.lower() == "hard":
        return -5
    else:
        return 0

def option_generator(options):
    """Prints a vertical list of options in all caps then gets user
    input"""
    print("\n")
    for i in options:
        print("> ", i.upper())
    print("\n")
    user_response = user_input(options)
    return user_response

def user_input(options):
    """Loops user to re-type their answer to match options"""
    loop = True
    while loop is True:
        user_says = input("> ")
        loop = verify_input(user_says, options)
    return user_says

def start():
    """Initiates the start of the game"""
    print("Hello! Welcome to this little adventure!")
    print("\nWhat is your name?\n")
    player_name = confirm_player_name(input("> "))
    player_name = player_name.title()
    print(f"\nWell {player_name}, let's get started.")
    return player_name

def confirm_player_name(name):
    print(f"You wrote {name.title()}, is this correct?")
    options = ["Yes", "No"]
    confirm = input("> ")
    if confirm.lower() == "yes":
        pass
    else:
        print("Please re-type your name:")
        name = input("> ")
        confirm_player_name(name)
    return name

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
        house_entrance()
    elif selection.lower() == "go to back":
        print("Going around to the back!")
        house_behind()
    else:
        print("Getting the heck outta here!")
        house_leave()

def house_behind():
    """Describes behind The House and available actions"""
    dead("You made it to the back of the house, congrats!")
# -> Look through windows - 3 choices
# -> Go back to front of house

def house_entrance():
    """Describes the first room of The House and available actions"""
    current_room = "house_entrance"
    if current_room in completed_rooms:
        pass
    else:
        print("First time description")
    print("House Entrance description")
    finish_room(current_room)
    show_options = ["Go left", "Go right", "Get out"]
    selection = option_generator(show_options)
    if selection.lower() == "go left":
        print("Opening the left door.")
        house_left()
    elif selection.lower() == "go right":
        print("Opening the right door")
        house_right()
    else:
        print("Trying to open the door, it cuts your hand. -1 HP")
#       Reduce health by 1
        house_entrance()
    dead("You made it into the house, congrats!")

def house_left():
    """Describes the Left Room of The House and available actions"""
    current_room = "house_left"
    if current_room in completed_rooms:
        pass
    else:
        print("First time description")
    print("Left Room generic description")
    finish_room(current_room)
    show_options = ["Go forward", "Go back", "Secret item"]
    selection = option_generator(show_options)
    if selection == "go forward":
#       Check if puzzle solved
        print("Going forward")
        house_back()
    elif selection == "go back":
        print("Going backwards")
        house_entrance()
    else:
        print("This will be related to the secret item")
#       check inventory for item
        if "Nothing" in inventory:
            update_inventory("Nothing", "remove")
#       add item
        update_inventory("secret_left", "add")
        print(inventory)
        house_left()
    dead("You made it into the left room of the house, congrats!")

def house_right():
    """Describes the Right Room and summons the Bear fight"""
    current_room = house_right
    if current_room in completed_rooms:
        print("Generic message about the room")
    else:
        print("This will be the introductory message to the room")
        print("Now summoning.... THE BEAR")
        summon_bear(10, False)
        finish_room(current_room)

    show_options = ["Go forward", "Go back", "Secret item"]
    selection = option_generator(show_options)
    if selection == "go forward":
        print("Going forward")
        house_back()
    elif selection == "go back":
        print("Going backwards")
        house_entrance()
    else:
        print("This will be related to the secret item")
#       check inventory for item
        if "Nothing" in inventory:
            update_inventory("Nothing", "remove")
#       add item
        update_inventory("secret_right", "add")
        print(inventory)
        house_right()
    dead("You made it into the right room of the house, congrats!")

def summon_bear(bear_health, bear_defeated):
    global player_health
    if bear_defeated is False:
        print(f"Current HP: {player_health}")
        show_options = ["Fight", "Defend"]
        selection = option_generator(show_options)
        if selection.lower() == "fight":
            print("You go in for a fight!")
            bear_health -= 3
            print("But it's a bear, and just swipes you too.")
            player_health -= 5
            print(f"Bear: {bear_health}. Player: {player_health}")
        elif selection.lower() == "defend":
            print("You try to defend yourself against a bear. It hurts.")
            player_health -= 2
        if bear_health <= 0:
            print("Bear down, bear down!!")
            bear_defeated = True
        else:
            summon_bear(bear_health, False)

# Actually could do a simple fight system:
#   Bear has 15? HP
#   Player has {player_health}  HP
#   FIGHT (-3 bear HP) | DEFEND (-2 user HP) maybe ATK//2?
#   BEAR does -5 HP per hit?
#       Maybe 1/3 chance attack, 2/3 chance nothing
#       This would mean death in 4/3/2 rounds...

def house_back():
    """Descibes the Back Room of The House and available actions"""
    dead("You made it into the back room of the house, congrats!")
#   Set up final puzzle
#   Check if player has both secret items
#   if both_items is True:
#       house_secret()
#   else:
#       victory()

def house_secret():
    """Describes the SECRET ROOM of The House, needs keys!"""
    dead("You made it into the secret room, congrats!!")
# Idea: Collect item from Left and Right to find
# Why? For fun!
# Some secret message or something! idk!

def house_leave():
    """Runs a x5 loop of getting "lost" the first time, then allows \
    exit"""
    current_room = "house_leave"
    if current_room in completed_rooms:
        print("You actually have your bearing now, and don't know how you got lost before.")
        victory()
    else:
        loop = True
    print("Generic description of the neighbourhood")

    while loop is True:
        for i in range(1,6):
            print(f"Repetitive description. You have seen this {i} times")
            input("> ")
            if i == 5:
                print(f"This is the {i}th time you've seen that decoration. You trace your steps, ending back at the house.")
                break
        loop = False
    finish_room(current_room)
    house_front()

def dead(why):
    """Prints the game over message and exits"""
    print(f"{why} Game over!")
    exit(0)
    
def victory():
    """Prints the victory end screen, showing totals, then exits"""
    print(f"Congratulations {player_name}! You left the neighbourhood with {player_health} HP!")
    print("Here's what you had in your pockets: {}".format(*inventory))
    print(f"Thank you for playing {player_name}!")
    exit(0)

room_list = ["house_front", "house_behind", "house_leave", "house_entrance," "house_left", "house_right", "house_final", "house_secret"]
inventory = ["Nothing"]
completed_rooms = []
main_menu()
player_health = player_health + difficulty()
print("Your starting health will be:", player_health, "HP\n")
player_name = start()
house_front()
