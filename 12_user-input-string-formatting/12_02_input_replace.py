# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

string_input = input("Please type a phrase: ") # User can write whatever they want
symbol_input = input("input a symbol: " ) # put whatever symbol they want

first_letter = string_input[0] #Get the first letter of whatever is typed 

print(string_input.replace(first_letter, symbol_input))


 #replaced what ever is type with the symbol

 #created a new string so I can call it out easier and just print it out when the script is done

