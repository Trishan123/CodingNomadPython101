# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input("What is your name " ) # put a variable down so that I can write

if " " in name:
    index = name.find(" ")
    name = name[0:index]
print("Welcome " + name)

#print(name)  #Next I want to print whatever the user writes in a seperator so if they put first and last name python will know to seperate them
      