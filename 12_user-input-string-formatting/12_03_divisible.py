# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

x = int(input("please enter a number  "))


if x <= 1 or x > 1_000_000_000:
    print("This number is not between 1 and 1,000,000,000")
else:
    
    if int(x) % 3 == 0:
        print("It is divisble by 3 " + str(x) )

    else:
        print("not divisble by 3" )
