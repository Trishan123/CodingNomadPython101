# Write a script that prints a star pyramid of flexible size
# If the `stars` variable is `5`, your code will output:
#
# *
# * *
# * * * 
# * * * *
# * * * * * 
#
# There should be five rows in total:
# 1. the 1st row will have 1 star,
# 2. the 2nd row will have 2 stars,
# 3. the 3rd row will have 3 stars,
# 4. the 4th row will have 4 stars,
# 5. the 5th row will have 5 stars
#
# Another example: if you set the `stars` variable tp `3`, 
# your code will output:
#
# *
# * *
# * * *
#
# HINT: Think of nested for loops!

stars = 5  # You can change this to any number for a different size pyramid

# Outer loop for each row
for i in range(1, stars + 1):
    # Inner loop to print stars on the current row
    for j in range(i):
        print("*", end=" ")  # Print star with a space, but don't go to a new line
    print()  # Move to the next line after each row
