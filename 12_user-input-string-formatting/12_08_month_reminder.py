# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.
month = int(input("Please select a number from 1 - 12 "))
if month == 1:
    print("You selected the month January")
elif month == 2:
    print("you selected the month Feburary")
elif month == 3:
    print("you selected the month March")
elif month == 4:
    print("you selected the month April")
elif month == 5:
    print("you selected the month May")
elif month == 6:
    print("you selected the month June")
elif month == 7:
    print("you selected the month July")
elif month == 8:
    print("you selected the month August")
elif month == 9:
    print("you selected the month September")
elif month == 10:
    print("you selected the month October")
elif month == 11:
    print("you selected the month November")
elif month == 12:
    print("you selected the month Decemeber")
else:
    print("You did not select a number from 1-12 please type it again")