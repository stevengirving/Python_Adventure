from sys import exit

# Adventure design!

prompt = ("> ")

# Start
def start():
    print("Hello, and welcome to this game!")
    player_name = define_player_name()
    print(f"""
         Time for an adventure {player_name}!
         You come across a house while out on a walk.
         The door is unlocked, open in fact.
         You could also see if there is anything around the back.
         Or maybe you should leave?
         """
         )

# Define player name
def define_player_name():
    print("What is your name?")
    return input(prompt)

# Room 1

# Room 2

# Room 3

def dead(why):
    print(f"{why}. Game over!")
    exit(0)
