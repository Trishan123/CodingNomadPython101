# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
name = input("What is your name? ")

count_name = name.count(name + "a, e ,i, o, u")

print(count_name)