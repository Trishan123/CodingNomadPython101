# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings
word1 = input("Please write a word ")
word2 = input("Please write a word ")
word3 = input("Please write a word ")

if len(word1) > len(word2) and len(word1) > len(word3):
    lon_word = word1
elif len(word2) > len(word3):
    lon_word = word2
else:
    lon_word = word3
#print(str(len(lon_word)) + ", " + lon_word)
print(f"{len(lon_word)}, {lon_word}")