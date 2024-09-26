# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"

filename = "operators.pdf"
last_four_chars = []
is_pdf = False  # Flag to indicate if it's a PDF file

for char in filename:
    # Append the current character
    last_four_chars.append(char)
    
    # If we have more than four characters, remove the oldest one
    if len(last_four_chars) > 4:
        # Remove the first character in the list
        last_four_chars.pop(0)

# Check if the last four characters are '.', 'p', 'd', 'f'
if len(last_four_chars) == 4:
    if (last_four_chars[0] == '.' and
        last_four_chars[1] == 'p' and
        last_four_chars[2] == 'd' and
        last_four_chars[3] == 'f'):
        is_pdf = True  # Set the flag to True if it matches

# Print the result
if is_pdf:
    print(f"{filename} is a PDF file.")
else:
    print(f"{filename} is not a PDF file.")
