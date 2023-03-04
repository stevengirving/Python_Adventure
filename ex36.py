from sys import exit

# Adventure design!

# Start message welcoming the player
    # Allow Y|N prompt to exit

# Define player name
    # Get user input

# Inventory system?
    # Honestly probably only like 2-3 items total
    # Two functions? One to Add, one to Remove?

# List of completed rooms?
    # Add room to list when completed to allow backtracking
    # Each room could check against the list for True, then provide alt description

# Front of House
    # -> Enter house
    # -> Go to back of house
    # -> Leave

# Back of House
    # -> Look through windows - 3 choices
    # -> Go back to front of house

# House Entrance
    # -> Left Door
    # -> Right Door
    # -> Entrance door, now locked

# House Left
    # Flag unsolved
    # Some sort of puzzle
    # Door locked until solved
    # Secret item?
    # -> House Back
    # -> House Entrance

# House Right

# House Back

# House... Secret????
    # Idea: Collect item from Left and Right to find
    # Why? For fun!

# Try to Leave
    # Loop x5 message of walking if loop is False
    # Return to start
    # set loop is True
    # Describe actual exit avoiding loop
    exit(0)

# Game Over Message
def dead(why):
    print(f"{why}. Game over!")
    exit(0)
