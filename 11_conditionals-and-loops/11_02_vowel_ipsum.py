# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

# Define the vowels
vowels = 'aeiouAEIOU'

# Initialize the counter
vowel_count = 0

# Iterate over each character in the text
for char in lorem_ipsum:
    if char in vowels:
        vowel_count += 1

# Print the total number of vowels
print("The total number of vowels in the text is:", vowel_count)