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
user1 = input("first word: ")
user2 = input("second word: ")
user3 = input("third word: ")


len_user1 = len(user1)
len_user2 =  len(user2)
len_user3 = len(user3)


if len_user1 > len_user2 and len_user1 > len_user3:
    print(str(len_user1) + ", "  + user1)
elif len_user2 > len_user1 and len_user2 > len_user3:
    print((len_user2), user2)
else:
    print(len_user3, user3)
