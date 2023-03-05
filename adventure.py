from sys import exit

# Adventure design!

# Start message welcoming the player
def start():
    print("Hello! Welcome to this little adventure!")
    player_name = get_player_name()
    print(f"{player_name}, let's get started.")
    return player_name

# Define player name
def get_player_name():
    print("What is your name?")
    return input("> ")

# Inventory system
# Honestly probably only like 2-3 items total
# Two functions? One to Add, one to Remove?
# def inventory(item, action):
#   if action is "add":
#       inventory.append(item)
#   elif action is "remove":
#       inventory.pop(item)
#   else:
#       pass

def finish_room(room):
    completed_rooms.append(room)

# Front of House
def house_front():
    current_room = house_front.__name__
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
    print(f"The house ")
    show_options = ["Go inside", "Go to back", "Leave"]
    choice = input(prompt)
    verify_input(choice, show_options)


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

# Function to move between rooms?
# def move_room(current_room, next_room):
#   

# Try to Leave
    # Loop x5 message of walking if loop is False
    # Return to start
    # set loop is True
    # Describe actual exit avoiding loop
    # exit(0)

# Game Over Message
def dead(why):
    print(f"{why}. Game over!")
    exit(0)
    
prompt = "> "
room_list = ["house_front", "house_back", "house_leave", "house_entrance," "house_left", "house_right", "house_final", "house_secret"]
inventory = []
completed_rooms = []
player_name = start()
house_front()
