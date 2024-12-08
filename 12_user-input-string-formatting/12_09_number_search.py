# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.
num = int(input("Please select a number from 0 - 1,000,000,000 "))
count_num = 0
while count_num != num:
    count_num += 1
print(count_num)
