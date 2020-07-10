from room import Room
from player import Player
from item import Item

# Declare items for rooms
pencil = Item("pencil", "is mightier than a sword")
knife = Item("knife", "is light-weight and sharp")
stick = Item("stick", "is thin and fragile")
rock = Item("rock", "is rough with jagged edges")
rope = Item("rope", "is long and useful when tied")
# ope = Item("rope", "is long and useful when tied")

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [pencil, knife, rope]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [stick, rock]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

    if player_start.current_room.items is not None:
        print("****************** \n Items Found!")

        for item in player_start.current_room.items:
            print(f"{item.name.upper()}: {item.description}")

        print("****************** \n Inventory Limit is 3:")

        if player_start.items is not None:
            for items in player_start.items:
                print(items.name.upper())
        else:
            print(" Your inventory is empty.")

    user_input = input(
        "****************** \n Enter a cardinal direction to explore. (N,E,S,W) \n To pickup an item type: 'take <Item Name Here>' \n To drop an item from inventory type: 'drop <Item Name Here>' \n Want To Quit The Game? (Q) \n What will you do? ").lower().split()

    if user_input[0] in ["n", "e", "s", "w"]:
        print(f"{user_name} heads toward...")
        player_start.move(user_input[0])
    elif user_input[0] == "take" and player_start.current_room.items and len(player_start.items) < 3:
        for i in range(0, len(player_start.current_room.items)):
            if user_input[1] == player_start.current_room.items[i].name:
                selected_item = player_start.current_room.items.pop(i)
                player_start.items.append(selected_item)
                continue
    elif user_input[0] == "drop" and len(player_start.items) > 0:
        for i in range(0, len(player_start.items)):
            if user_input[1] == player_start.items[i].name:
                player_start.items.pop(i)
                continue
    elif user_input[0] == "q":
        print(f"Goodbye {user_name}...")
        user_is_playing = False
    else:
        print("The Key You Entered Is Invalid. Please use N,E,S,W")
