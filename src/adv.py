from room import Room
from player import Player
from item import Item

# Declare items for rooms
pencil = Item("pencil", "is mightier than a sword")
knife = Item("knife", "is light-weight and sharp")
stick = Item("stick", "is thin and fragile")
rock = Item("rock", "is rough with jagged edges")
rope = Item("rope", "is long and useful when tied")

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", pencil),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", knife),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", stick),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", rock),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", rope),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user_name = input("Enter your name: ")
player_start = Player(user_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

user_is_playing = True

while user_is_playing:
    print(player_start.current_room.name)

    print(player_start.current_room.description)

    print(f"A {player_start.current_room.items.name} is on the floor, it {player_start.current_room.items.description}")

    user_input = input(
        " Enter a cardinal direction to explore. (N,E,S,W) \n Want To Quit The Game? (Q) \n What will you do? ").lower()

    if user_input in ["n", "e", "s", "w"]:
        print(f"{user_name} heads toward...")
        player_start.move(user_input)
    elif user_input == "q":
        print(f"Goodbye {user_name}...")
        user_is_playing = False
    else:
        print("The Key You Entered Is Invalid. Please use N,E,S,W")
