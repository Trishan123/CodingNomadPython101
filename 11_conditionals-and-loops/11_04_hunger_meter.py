# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.


#hunger = 2
hunger = "big"
if type(hunger) == str: # this is an if statment to hunger equaling with the type that was put in the input


    if hunger == "big":
      print("Eat the pizza")
    elif hunger == "small":
        print("Eat the apple")
    else:
        print("Don't eat anything")
else:
    print("Make sure this is a string")