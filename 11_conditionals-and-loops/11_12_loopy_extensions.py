# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf" # creating a variable to the .pdf
flag = False # making a variable thats a boolean flag, True if we see a period
word = "" # making an extension 
for character in filename: # iteratoring a character in filename
    if character == ".": # this equals to . in .pdf
        flag = True
    if flag == True:    
        word += character

if word == ".pdf":
    print("this is a .pdf")
else:
    print("not a pdf")