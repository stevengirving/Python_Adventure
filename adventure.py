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
    print(f"\nYou wrote {name.title()}, is this correct?\n")
    options = ["Yes", "No"]
    confirm = input("> ")
    if confirm.lower() == "yes":
        pass
    else:
        print("\nPlease re-type your name:\n")
        name = input("> ")
        confirm_player_name(name)
    return name


def update_inventory(item, action):
    """System to add or remove items to the inventory list"""
    if "Nothing" in inventory:
        inventory.remove("Nothing")
    else:
        pass
    if action == "add":
       inventory.append(item)
    elif action == "remove":
       inventory.remove(item)
    else:
       dead("Something messed up with update_inventory")

    if inventory == False:
        inventory.append("Nothing")
    else:
        pass

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

# TODO
def puzzle_note(file):
    global puzzle_version
    with open(file), puzzle_version as f, p:
        for i, line in enumerate(f, start=1):
            if i == p:
                puzzle_line = print(line)
            elif i > 5:
                break
            else:
                dead("puzzle_note error!")

def house_front():
    """Initial scene of the game"""
    current_room = "house_front"
    if current_room in completed_rooms:
        pass
    else:
        print("""
    You are out on a walk one day when you come across a house you
    have never seen before. Oddly enoguh, you don't even recognize
    the neighbourhood you're in. You take a closer look at the house.

    The house itself seems to be abandoned, at least you cannot 
    see any lights on. The front door lays open, though perhaps
    the owner simply forgot it open while doing yardwork? They
    could be in the backyard, why not check. Though the front door
    is awfully inviting...   
    """
        )
        finish_room(current_room)
    print(f"""
    Generic message for {current_room}
    """
    )
    show_options = ["Go inside", "Go to back", "Leave"]
    selection = option_generator(show_options)
    if selection.lower() == "go inside":
        print("Going inside!\n")
        house_entrance()
    elif selection.lower() == "go to back":
        print("Going around to the back!\n")
        house_behind()
    else:
        print("Getting the heck outta here!\n")
        house_leave()


def house_behind():
    """Lets the user get a sneak peek at two rooms"""
    current_room = "house_behind"
    if current_room in completed_rooms:
        pass
    else: 
        print("First time description")
        completed_rooms.append(current_room)
    print("\nGeneric description\n")
    print(f"""
    Generic message for {current_room}
    """)
    show_options = ["Left Window", "Right Window", "Go back"]
    selection = option_generator(show_options)
    if selection.lower() == "left window":
        print("Left window, you see... a bear???")
    elif selection.lower() == "right window":
        print("Right window, you see a lot of papers scattered around the room.")
    else:
        print("\nYeah this is weird, you walk back to the front of the house.\n")
        house_front()
    house_behind()
    dead("You made it to the back of the house, congrats!")


def house_entrance():
    """Simple choice room with a chance to harm the player"""
    current_room = "house_entrance"
    global player_health
    if current_room in completed_rooms:
        pass
    else:
        print(f"""
        Generic message for {current_room}
        """
        )
    print(f"""
    Generic message for {current_room}
    """)
    finish_room(current_room)
    show_options = ["Go left", "Go right", "Get out"]
    if "Front Door Key" in inventory:
        show_options.remove("Get out")
        show_options.append("Get out with key")
    selection = option_generator(show_options)
    if selection.lower() == "go left":
        print("Opening the left door.\n")
        house_left()
    elif selection.lower() == "go right":
        print("Opening the right door\n")
        house_right()
    elif selection.lower() == "get out with key":
        print("You manage to unlock the front door, and step outside")
        house_front()
    else:
        print("Trying to open the door, it cuts your hand. -1 HP")
        player_health -= 1
        if player_health <= 0:
            dead("You manage to die via door, congrats.")
        else:
            house_entrance()
    dead(f"Error at {current_room}")


def house_left():
    """Puzzle room based on reading text files """
    global puzzle_solved
    global puzzle_started
    current_room = "house_left"
    if current_room in completed_rooms:
        print(f"""
        Generic message for {current_room}
         """
        )
    elif puzzle_started is False:
        print("First time introduction to the room and puzzle.\n")
        puzzle_started = True
        start_puzzle()
    elif puzzle_started is True and puzzle_solved is False:
        print("The puzzle is still sitting here, waiting for you.\n")
    else:
        pass

    if puzzle_solved == True:
        finish_room(current_room)
    else:
        show_options = ["Look at puzzle", "Go back"]
        selection = option_generator(show_options)
        if selection.lower() == "look at puzzle":
            print("You study the papers on the table and try to figure it out once more.\n")
            start_puzzle()
        elif selection.lower() == "go back":
            print("You leave this room and go back to the entrance.\n")
            house_entrance()
        else:
            pass

    print("Left Room generic description\n")
    show_options = ["Go forward", "Go back", "Secret item"]
    if "Paper Key" in inventory:
        show_options.remove("Secret item")
    else:
        pass
    selection = option_generator(show_options)
    if selection == "go forward":
        print("Going forward\n")
        house_back()
    elif selection == "go back":
        print("Going backwards\n")
        house_entrance()
    else:
        print("This will be related to the secret item\n")
        update_inventory("Paper Key", "add")
        house_left()
    dead(f"Error at {current_room}")


# TODO
def start_puzzle():
    """Lets the user read over five files and then try a solution"""
    print("While there are plenty of papers scattered around, there are five in particular that catch your attention.\n")
    if puzzle_solved == False:
        show_options = ["File one", "File two", "File three", "File four", "File five", "Solve Puzzle", "Go back"]
        files = {"File one": "note1.txt", "File two": "note2.txt", "File three": "note3.txt", "File four": "note4.txt", "File five": "note5.txt"}
        selection = option_generator(show_options)
        for show_options in files:
            if selection.lower() == show_options.lower():
                choice = files[show_options]
                print(choice)
                read_file(choice)
                start_puzzle()
            else:
                pass
        if selection.lower() == "solve puzzle":
            print("You think you have this figured out...\n")
            solve_puzzle()
            house_left()
        else:
            print("You leave the puzzle alone for now.\n")
    else:
        pass
    house_left()
   
# TODO
def read_file(file):
    global puzzle_version
    puzzle_file = open(file, 'r').readlines()
    for x in puzzle_file:
        if x[:2].strip() == str(puzzle_version):
            print(str(x[2:]))
        else:
            pass
    else:
        pass

def solve_puzzle():
    """Lets the user try to solve the puzzle"""
    global puzzle_solved
    puzzle_solution = "???"
    print("From the clues given, what do you think the solution is?\n")
    user_guess = input("> ")
    if user_guess.lower() == puzzle_solution:
        print("Nice, you solved the puzzle!")
        puzzle_solved = True
        house_left()
    else:
        print(f"You try to type {user_guess}, but it fails.\n")


def house_right():
    """Initiates a simple fight against a bear"""
    current_room = "house_right"
    global summoned_bear
    if current_room in completed_rooms:
        print("Generic message about the room")
    elif summoned_bear is False:
        print("Now summoning... THE BEAR\n")
        summoned_bear = True
        summon_bear()
    else:
        print("The bear is still here, and doesn't seem keen to leave.\n")
        summon_bear()

    if bear_defeated == True:
        finish_room(current_room)
    else:
        pass
    show_options = ["Go forward", "Go back", "Secret item"]
    if "Bear Key" in inventory:
        show_options.remove("Secret item")
    else:
        pass
    selection = option_generator(show_options)
    if selection == "go forward":
        print("Going forward")
        house_back()
    elif selection == "go back":
        print("Going backwards")
        house_entrance()
    else:
        print("This will be related to the secret item\n")
        update_inventory("Bear Key", "add")
        house_right()
    dead(f"Error at {current_room}")


def summon_bear():
    """Loops through combat options until either player or bear are dead"""
    global player_health
    global player_name
    global bear_defeated
    global bear_health
    if bear_defeated is False:
        show_options = ["Fight", "Defend", "Flee"]
        selection = option_generator(show_options)
        if selection.lower() == "fight":
            print("You go in for a fight!\n")

            player_hit_roll = randint(1,3)
            if player_hit_roll == 2:
                print("You get closer to the bear, trying to fight an angle to punch it.\n")
            else:
                print("You manage to get close to the bear, and smack its snoot.\n")
                bear_health -= 3
                    
            bear_hit_roll = randint(1,3)
            if bear_hit_roll == 2:
                print("But it's a bear, and just swipes you with its claws.\n")
                player_health -= 5
            else:
                print("Surprisingly, you're able to back away as the bear tries to hit you.\n")

        elif selection.lower() == "defend":
            print("You try to defend yourself against a bear. It hurts.\n")
            player_health -= 2

        elif selection.lower() == "flee":
            print("You sprint back to the door and try to open it.\n")
            x = randint(1,20)
            if x <= 20:
                print("You manage to open the door, and get out!\n")
                house_entrance()
            else:
                print("In your panic, you can't open the door! The bear comes for you!\n")
                player_health -= 5
                

        if bear_health <= 0 and player_health <= 0:
            dead(f"In a heroic action, {player_name} used their final breath to slay the bear.")
        elif player_health <= 0:
            dead(f"As expected, you have died to a bear. Good job {player_name}.")
        elif bear_health <= 0:
            print("Bear down, bear down!!")
            bear_defeated = True
        else:
            summon_bear()


def house_back():
    """Has front entrance key; checks if players have both secret items"""
    current_room = "house_back"
    if current_room in completed_rooms:
        pass
    else:
        print("House Back first time description.\n")
        print("Added Front Door Key to inventory\n")
        inventory.append("Front Door Key")
        finish_room(current_room)

    print("House Back generic description")
    show_options = ["Open left door", "Open right door"]
    if "Paper Key" in inventory and "Bear Key" in inventory:
        show_options.append("Open secret drawer")
    else:
        pass
        
    if "house_left" in completed_rooms:
        show_options.remove("Open left door")
        show_options.append("Open paper door")
    else:
        pass

    if "house_right" in completed_rooms:
        show_options.remove("Open right door")
        show_options.append("Open bear door")
    else:
        pass

    selection = option_generator(show_options)
    if selection.lower() == "open right door" or selection.lower() == "open bear door":
        print("opening the right door\n")
        house_right()
    elif selection.lower() == "open left door" or selection.lower() == "open paper door":
        print("opening the left door\n")
        house_left()
    elif selection.lower() == "open secret drawer":
        print("Congrats on getting both secrets!\n")
        house_secret()

    dead(f"Error at {current_room}")


def house_secret():
    """SECRET DRAWER which needs two keys to open; just an easter egg"""
    print("You made it into the secret drawer, congrats!!\n")
    house_back()


def house_leave():
    """Runs a x5 loop of getting "lost" the first time, then allows exit"""
    global leave_count
    current_room = "house_leave"
    if "Front Door Key" in inventory:
        print("\nYou actually have your bearing now, and don't know how you got lost before.\n")
        victory()
    else:
        print("Generic description of the neighbourhood")
        for i in range(1,6):
            leave_count += 1
            print(f"\nRepetitive description. You have seen this {i} times\n")
            input("> ")
            if i == 5:
                print(f"\nYou've seen that decoration {leave_count} times total now... You trace your steps, ending back at the house.\n")
                break
    house_front()


def dead(why):
    """Prints the game over message and exits"""
    print(f"\n{why} Game over!")
    exit(0)


def victory():
    """Prints the victory end screen, showing totals, then exits"""
    print(f"Congratulations {player_name}! You left the neighbourhood with {player_health} HP!\n")
    print("Here's what you had in your pockets:", ", ".join(inventory))
    print(f"\nThank you for playing {player_name}!\n")
    exit(0)


room_list = ["house_front", "house_behind", "house_leave", "house_entrance," "house_left", "house_right", "house_back", "house_secret"]
inventory = ["Nothing"]
completed_rooms = []
bear_defeated = False
summoned_bear = False
bear_health = 10
puzzle_solved = False
puzzle_started = False
puzzle_version = randint(1,5)
leave_count = 0
main_menu()
player_health = player_health + difficulty()
print("Your starting health will be:", player_health, "HP\n")
player_name = start()
house_front()
