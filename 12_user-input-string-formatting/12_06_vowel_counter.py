# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
name = input("What is your name? ").lower()
vowels = "aeiou"
count_name = 0

for vowel in vowels:
    count_name += name.count(vowel)

print(count_name)