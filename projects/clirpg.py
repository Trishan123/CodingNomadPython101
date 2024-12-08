# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

player = input("What is your name? ") #player puting there name
print("Welcome " + player + " To the game of dungeon and dragons!") # printing out the player plus entering the game
Dragon_room = "Dragon room" # this is where the dragon will be
hallway = "hallway"
has_sword = False # the is the variable that the player will carry the sword
Sword_room = "sword room" # this is the room where the sword will be 
action_sword = "picking up the sword" # this is the action for the player to pick up the sword
dragon_is_slain = False
location = hallway # this is where the player will go in between to the rooms
while dragon_is_slain != True:
    while location == hallway: # this 
        print("You are in the hallway")
        choice = input("Would you like to go left or right?")
        if choice == "left":
            print("You went left")
            location = Sword_room
        elif choice == "right":
            print("You went right")
            location = Dragon_room
        
        else:
            print("Nothing happened")

    while location == Sword_room:
        action_sword = input("do you want to pick up the sword or leave the room?")
        if action_sword == "yes":
            has_sword = True
            print("you picked up the sword")
        elif action_sword == "no":
            location = hallway
            print("you have left the room ")   
        else:
            print("wrong choice")
    
    while location == Dragon_room:
        dragon = input("do you want to fight the dragon please select yes or no ")
        if dragon == "yes" and has_sword:
            dragon_is_slain = True
            location = "victory room"
            print("you have slain the the dragon")
        else:
            print("you have lost to the dragon please try again")
            location = hallway

print("hooray " + player + " you have won the game")