# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
word = input("what do you think of the sky? ") # creating the user input
alt_word = "" # creating an empty string for this variable
#print(word[0].upper())
#print(word[1].lower())
#print(word[2].upper())
should_upper = True

for letter in word:
    if should_upper: 
        alt_word += letter.upper()
        should_upper = False
    else:
        alt_word += letter.lower()  
        should_upper = True

"""count_word = 0
while len(alt_word) != len(word):
    
    letter = word[count_word]  

    if should_upper:
        alt_word += letter.upper()
        should_upper = False
    else:
        alt_word += letter.lower()
        should_upper = True
    
    count_word += 1 """
print(alt_word)