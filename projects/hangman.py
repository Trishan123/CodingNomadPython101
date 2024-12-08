# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

hanging_man_word = "food" # this is a variable for the guessing word
under_scores = "_ " * len(hanging_man_word) # this is another variable to mark how many letters are there
guess_count = 0
print("""Welcome to the Hangman game""") 
while True:
    if not "_" in under_scores: # this is to say _ not in the variable in under_scores
        print("yayyyyy the correct word is: " + hanging_man_word) # printed the statement
        break # breaks out of the while loop
    if guess_count >= 5: #  amount of incorrect tries nothing higher than 5
        print("Sorry you ran out of attemps, the correct word is: " + hanging_man_word) # printed out a statement for to many incorrect guesses
        break # breaks out of the while loop
    print(under_scores, "Here is the amount you have tried: " + str(guess_count))
    letter = input("type a letter? ") 
    if len(letter) == 1 and letter.isalpha():
       # User has enter a single letter and was able to only work if its alphbetical and not numerical or spaces 
        if letter in hanging_man_word:
            #this is saying you guess the correct letter in the variable
            print("Good job you got the right letter: " + letter) # Prints out the correct letter with a statement letting the user know that it is correct  
            for i in range(len(hanging_man_word)): # counting from 0 to the len of the variable
                #print(i)      
                if hanging_man_word[i] == letter: # used the count that matches with the input variable at that position
                     under_scores = under_scores[0:i*2] + letter + under_scores[i*2+1:] # this replaced the letter that was showing as a under bracket
        else: # this else is for incorrect guess
            guess_count += 1 # counting for the amount incorrect guess
            print("ooooooo try again") # this printed out a statement for the user to know its not correct
    else: # user entered a incorrect letter
        print("Ooops you didn't type one letter try again") # user didn't put only one letter
print("Thanks for playing the game")

    
